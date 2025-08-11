const fs = require('fs');
const path = require('path');
const yargs = require('yargs');

// Configure yargs to accept named command-line arguments
const argv = yargs
    .option('input', {
        alias: 'i',
        description: 'Path to the input JSON file',
        type: 'string',
        demandOption: true,
    })
    .option('output', {
        alias: 'o',
        description: 'Path to the output JSON file',
        type: 'string',
        demandOption: true,
    })
    .option('fieldnames', {
        alias: 'f',
        description: 'Comma-separated list of field names to include in the output',
        type: 'string',
        demandOption: false,
    })
    .help()
    .alias('help', 'h')
    .argv;

const inputFilePath = path.resolve(argv.input);
const outputFilePath = path.resolve(argv.output);
const extractFieldList = argv.fieldnames.split(",");

// Function to process the JSON data
function processData(inputData) {
    const deepCopy = [];
    for (key of Object.keys(inputData)) {
        deepCopy.push(
            {
                Symbol: key,
                Web: `https://www.google.com/finance/quote/${key}:NYSE`,
                ...extractFieldList.reduce((filtered, field) => {
                    if (inputData[key].hasOwnProperty(field)) {
                        filtered[field] = inputData[key][field];
                    }
                    return filtered;
                }, {}),
            }
        );
    }
    return deepCopy.sort((a, b) => (a.trailingPE || 200000) - (b.trailingPE || 200000));
}

// Main function to read, process, and write JSON data
function processJsonFile(inputFilePath, outputFilePath) {
    try {
        // Read the input JSON file
        const rawData = fs.readFileSync(inputFilePath, 'utf8');
        const jsonData = JSON.parse(rawData);

        // Process the data
        const processedData = processData(jsonData);

        // Write the processed data to the output file
        fs.writeFileSync(outputFilePath, JSON.stringify(processedData, null, 2), 'utf8');
        console.log(`Processed data has been written to ${outputFilePath}`);
    } catch (error) {
        console.error('Error processing JSON file:', error.message);
    }
}

// Use the command-line arguments

processJsonFile(inputFilePath, outputFilePath);