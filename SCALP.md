# Range-Scalp Bot

*Updated Sun Nov 15 01:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60126 | 52446 | 7680 (107) | 0 | $-16376.25 | -4.3% |
| **+10¢** | 44925 | 35924 | 9001 (143) | 0 | $-15473.65 | -5.5% |
| **+15¢** | 37641 | 27935 | 9706 (181) | 0 | $-14119.95 | -6.0% |
| **+20¢** | 33540 | 23357 | 10183 (233) | 0 | $-12456.08 | -5.9% |
| **+10¢ (15¢ stop)** | 73201 | 73058 | 143 (82) | 0 | $-26921.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 01:07 | +10 stop | NEAR | DOWN | 0.71 | 0.90 | 1.71 |
| 11-15 01:07 | +20 | NEAR | DOWN | 0.71 | 0.95 | 2.17 |
| 11-15 01:07 | +15 | NEAR | DOWN | 0.71 | 0.90 | 1.71 |
| 11-15 01:05 | +10 stop | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 11-15 01:05 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.79 |
| 11-15 01:05 | +15 | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 11-15 01:05 | +10 | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 11-15 01:05 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 11-15 01:05 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-15 01:01 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-15 01:01 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-15 01:01 | +15 | ZEC | DOWN | 0.69 | 0.89 | 1.81 |
| 11-15 01:01 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.97 |
| 11-15 01:01 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-15 01:01 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-15 01:01 | +20 | BNB | DOWN | 0.65 | 0.86 | 1.85 |
| 11-15 01:01 | +15 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 11-15 01:01 | +10 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 11-15 01:01 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 11-15 01:01 | +10 stop | ETH | DOWN | 0.58 | 0.82 | 2.11 |
| 11-15 01:01 | +20 | ETH | DOWN | 0.58 | 0.82 | 2.11 |
| 11-15 01:01 | +15 | ETH | DOWN | 0.58 | 0.82 | 2.11 |
| 11-15 01:01 | +10 | ETH | DOWN | 0.59 | 0.82 | 2.02 |
| 11-15 01:01 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 11-15 01:01 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-15 01:01 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-15 01:01 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 01:01 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-15 01:01 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-15 01:01 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-15 01:01 | +20 | HYPE | DOWN | 0.63 | 0.84 | 1.83 |
| 11-15 01:01 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-15 01:01 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-15 01:01 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-15 01:01 | +10 stop | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 01:01 | +20 | NEAR | DOWN | 0.65 | 0.88 | 2.06 |
| 11-15 01:01 | +15 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 01:01 | +10 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-15 01:01 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-15 01:01 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
