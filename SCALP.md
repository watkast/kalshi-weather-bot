# Range-Scalp Bot

*Updated Thu Oct 29 01:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38786 | 33848 | 4938 (49) | 0 | $-10877.17 | -4.5% |
| **+10¢** | 28933 | 23230 | 5703 (71) | 0 | $-9637.98 | -5.3% |
| **+15¢** | 24206 | 18079 | 6127 (97) | 0 | $-8583.14 | -5.6% |
| **+20¢** | 21475 | 15057 | 6418 (125) | 0 | $-7495.31 | -5.6% |
| **+10¢ (15¢ stop)** | 47429 | 47362 | 67 (35) | 0 | $-17983.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 01:47 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 10-29 01:47 | +10 stop | BNB | DOWN | 0.57 | 0.74 | 1.38 |
| 10-29 01:47 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-29 01:47 | +10 stop | SOL | DOWN | 0.56 | 0.73 | 1.38 |
| 10-29 01:47 | +10 stop | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-29 01:47 | +20 | HYPE | DOWN | 0.65 | 0.94 | 2.67 |
| 10-29 01:47 | +15 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-29 01:47 | +10 | HYPE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-29 01:47 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.60 |
| 10-29 01:47 | +10 stop | NEAR | DOWN | 0.67 | 0.89 | 1.97 |
| 10-29 01:47 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-29 01:47 | +15 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-29 01:47 | +10 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 10-29 01:47 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 10-29 01:46 | +10 stop | XRP | DOWN | 0.57 | 0.41 | -1.95 |
| 10-29 01:46 | +20 | XRP | DOWN | 0.57 | 0.87 | 2.74 |
| 10-29 01:46 | +15 | XRP | DOWN | 0.57 | 0.87 | 2.74 |
| 10-29 01:46 | +10 | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 10-29 01:46 | +5 | XRP | DOWN | 0.57 | 0.66 | 0.56 |
| 10-29 01:46 | +10 stop | DOGE | DOWN | 0.66 | 0.44 | -2.54 |
| 10-29 01:46 | +20 | DOGE | DOWN | 0.66 | 0.94 | 2.64 |
| 10-29 01:46 | +15 | DOGE | DOWN | 0.68 | 0.94 | 2.44 |
| 10-29 01:46 | +10 | DOGE | DOWN | 0.70 | 0.94 | 2.25 |
| 10-29 01:46 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-29 01:46 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-29 01:46 | +20 | BTC | DOWN | 0.63 | 0.87 | 2.15 |
| 10-29 01:46 | +15 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 01:46 | +10 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 01:46 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-29 01:46 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.25 |
| 10-29 01:46 | +20 | BNB | DOWN | 0.64 | 0.89 | 2.26 |
| 10-29 01:46 | +15 | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 01:46 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 01:46 | +5 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 01:46 | +10 stop | ETH | DOWN | 0.63 | 0.47 | -1.95 |
| 10-29 01:46 | +20 | ETH | DOWN | 0.63 | 0.86 | 2.04 |
| 10-29 01:46 | +15 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-29 01:46 | +10 | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-29 01:46 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-29 01:46 | +10 stop | SOL | DOWN | 0.66 | 0.48 | -2.14 |
