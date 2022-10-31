# Mini warngling for a school decision
## Brief
Robert has just finished his military service progress, he is now looking for opportunities to apply for university having Management Systems and Information Technology program.

Robert's criterias following as:

1. Safe places - low ratio of crime.
2. Metropolitian area - Robert prefer city vibes to peaceful lifestyle.
3. Entrepreneurship - University having top rank in startups.

## My solution
- **'Crime':** Calculate the total number of crime and take the school under 50th percentile of crime number.
- **'University':** Filter school having IT programs, and urban locations.
- **'Rank':** Take the < 25th percentile of ranking. Please notice that the higher number indicates lower ranking.
- **Merging 3 tables**: Join them together, then sort to find the most appropriate school.

## Library & syntax
```
pandas
pandas.DataFrame #Functions
```
