# Range-Scalp Bot

*Updated Mon Oct 19 18:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24387 | 21217 | 3170 (31) | 0 | $-7202.33 | -4.7% |
| **+10¢** | 18334 | 14673 | 3661 (46) | 0 | $-6437.21 | -5.6% |
| **+15¢** | 15354 | 11414 | 3940 (69) | 0 | $-5801.06 | -6.0% |
| **+20¢** | 13588 | 9463 | 4125 (87) | 0 | $-5204.29 | -6.1% |
| **+10¢ (15¢ stop)** | 29991 | 29939 | 52 (30) | 0 | $-11372.76 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 18:19 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-19 18:19 | +10 | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-19 18:19 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-19 18:19 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-19 18:19 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-19 18:19 | +5 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-19 18:17 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-19 18:16 | +5 | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-19 18:16 | +10 stop | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +15 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +10 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-19 18:16 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 10-19 18:16 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 18:16 | +20 | NEAR | DOWN | 0.62 | 0.83 | 1.83 |
| 10-19 18:16 | +15 | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 10-19 18:16 | +10 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 18:16 | +5 | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 18:16 | +10 stop | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-19 18:16 | +20 | BTC | DOWN | 0.59 | 0.86 | 2.44 |
| 10-19 18:16 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-19 18:16 | +10 | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 10-19 18:16 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-19 18:16 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 18:16 | +20 | BNB | DOWN | 0.67 | 0.89 | 1.97 |
| 10-19 18:16 | +15 | BNB | DOWN | 0.67 | 0.89 | 1.97 |
| 10-19 18:16 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-19 18:16 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 10-19 18:16 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-19 18:16 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 10-19 18:16 | +15 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 10-19 18:16 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-19 18:16 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-19 18:16 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-19 18:16 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 10-19 18:16 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-19 18:16 | +10 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-19 18:16 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-19 18:04 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.81 |
| 10-19 18:04 | +20 | XRP | UP | 0.64 | 0.87 | 2.07 |
