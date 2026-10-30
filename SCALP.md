# Range-Scalp Bot

*Updated Fri Oct 30 18:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41106 | 35881 | 5225 (53) | 0 | $-11455.26 | -4.4% |
| **+10¢** | 30635 | 24591 | 6044 (76) | 0 | $-10179.93 | -5.3% |
| **+15¢** | 25610 | 19098 | 6512 (103) | 0 | $-9232.59 | -5.7% |
| **+20¢** | 22731 | 15909 | 6822 (133) | 1 | $-8130.67 | -5.7% |
| **+10¢ (15¢ stop)** | 50119 | 50049 | 70 (37) | 0 | $-18937.57 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 18:20 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 18:20 | +15 | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 10-30 18:20 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 18:20 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 10-30 18:17 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 10-30 18:17 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 10-30 18:17 | +20 | BNB | DOWN | 0.71 | open |  |
| 10-30 18:17 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-30 18:17 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-30 18:17 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-30 18:17 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 10-30 18:16 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-30 18:16 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-30 18:16 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 10-30 18:16 | +15 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-30 18:16 | +10 | XRP | DOWN | 0.68 | 0.80 | 0.92 |
| 10-30 18:16 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 10-30 18:16 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 18:16 | +20 | ZEC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-30 18:16 | +15 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-30 18:16 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 18:16 | +5 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 18:16 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-30 18:16 | +20 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 10-30 18:16 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-30 18:16 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-30 18:16 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-30 18:16 | +10 stop | HYPE | DOWN | 0.64 | 0.78 | 1.11 |
| 10-30 18:16 | +20 | HYPE | DOWN | 0.64 | 0.85 | 1.85 |
| 10-30 18:16 | +15 | HYPE | DOWN | 0.64 | 0.79 | 1.22 |
| 10-30 18:16 | +10 | HYPE | DOWN | 0.64 | 0.78 | 1.11 |
| 10-30 18:16 | +5 | HYPE | DOWN | 0.64 | 0.78 | 1.11 |
| 10-30 18:16 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-30 18:16 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.91 |
| 10-30 18:16 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-30 18:16 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 10-30 18:16 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-30 18:15 | +10 stop | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-30 18:15 | +20 | BTC | DOWN | 0.57 | 0.80 | 2.00 |
| 10-30 18:15 | +15 | BTC | DOWN | 0.56 | 0.74 | 1.48 |
