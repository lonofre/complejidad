# Prectice 2: Verification Algorithms

## Computational Complexity 2024-1

Implementation of a verification algorithm and a generator of random certificates for the SIMPLE ROUTE problem. 

## Execution

For execution, you must have installed `python 3.8` or greater. Then, go to the root directory:

``` shell
cd src/
```

### Generation
To generate a random certificate, use the program `certificate_gen.py`: 

``` shell
python certificate_gen.py [INPUT_SAMPLE] [TARGET]
```
where: 
- `[INPUT_SAMPLE]` is a file containing the sample using the codification of the previous practice. 
- `[TARGET]`is the desired path to file where the certificate will be written. 

Some examples of generated certificates can be found at `certificates/` directory, using the samples in the 
`samples/` directory.

### Validation 
To validate if a sample given a randomly generated certificate belongs to the problem, use the program:
`validate.py`:
``` shell
python validate.py [INPUT_SAMPLE] [INPUT_CERTIFICATE]
```
where: 
- `[INPUT_SAMPLE]` is a file containing the sample using the codification of the previous practice. 
- `[INPUT_CERTIFICATE]`is a previously generated certificate.

The output will show: 
- Graph: A representation of the decoded input graph using adyacency list.
- Certificate: the decoded certificate.
- Route: A simple route, if possible. 
- k: the $k$ of the input sample. 
- is valid?: `True` if the sample with the certificate belongs to the problem, `False` otherwise. 

## Developed with :blue_heart: by
- López Carrillo Alan Ignacio
- Medel Piña Alberto Natanael
- Onofre Franco José Luis 
