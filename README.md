# JMath

JMath is a python utility to process math/logic statements stored in JSON.

Operations are stored as dictionaries in the JSON file and the operands are stored in arrays.

Operations can be nested with the child operations passing their results up the chain to the parent statement when processed.

## Example

```
Operation: (4 x 3) + 5

{
    "+": [
        {
            "x": [
                4,
                3
            ]
        },
        5
    ]
}

Result: 17
```

## Supported operations:

| Operation      | Key |
| -------------- | --- |
| Addition       | +   |
| Subtraction    | -   |
| Multiplication | x   |
| Division       | /   |
| Boolean AND    | AND |
| Boolean OR     | OR  |
| Boolean XOR    | XOR |
| Greater than   | >   |
| Less than      | <   |
| Equals         | =   |

## Supported functions:

| Function | Name     |
| -------- | -------- |
| Sum      | jm_sum   |
| Count    | jm_count |


