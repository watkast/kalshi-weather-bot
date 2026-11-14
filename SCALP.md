# Range-Scalp Bot

*Updated Sat Nov 14 16:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59532 | 51942 | 7590 (107) | 3 | $-16103.56 | -4.3% |
| **+10¢** | 44465 | 35577 | 8888 (142) | 3 | $-15154.13 | -5.4% |
| **+15¢** | 37262 | 27678 | 9584 (178) | 3 | $-13792.40 | -5.9% |
| **+20¢** | 33192 | 23133 | 10059 (230) | 3 | $-12172.04 | -5.8% |
| **+10¢ (15¢ stop)** | 72438 | 72295 | 143 (82) | 0 | $-26647.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 16:08 | +10 stop | XRP | DOWN | 0.71 | 0.90 | 1.70 |
| 11-14 16:05 | +15 | BTC | DOWN | 0.64 | 0.82 | 1.52 |
| 11-14 16:05 | +10 | BTC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-14 16:04 | +10 stop | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-14 16:04 | +5 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-14 16:03 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 11-14 16:03 | +10 stop | BNB | DOWN | 0.65 | 0.94 | 2.65 |
| 11-14 16:03 | +10 | BNB | DOWN | 0.65 | 0.94 | 2.65 |
| 11-14 16:03 | +5 | ZEC | UP | 0.52 | open |  |
| 11-14 16:03 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.20 |
| 11-14 16:02 | +10 stop | HYPE | DOWN | 0.66 | 0.40 | -2.93 |
| 11-14 16:02 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 16:02 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-14 16:02 | +10 stop | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 11-14 16:02 | +20 | ETH | DOWN | 0.58 | 0.78 | 1.70 |
| 11-14 16:02 | +15 | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 11-14 16:02 | +10 | ETH | DOWN | 0.58 | 0.75 | 1.38 |
| 11-14 16:02 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 11-14 16:01 | +10 stop | BNB | DOWN | 0.52 | 0.64 | 0.85 |
| 11-14 16:01 | +20 | BNB | DOWN | 0.52 | 0.72 | 1.67 |
| 11-14 16:01 | +15 | BNB | DOWN | 0.52 | 0.72 | 1.67 |
| 11-14 16:01 | +10 | BNB | DOWN | 0.52 | 0.64 | 0.85 |
| 11-14 16:01 | +5 | BNB | DOWN | 0.52 | 0.58 | 0.24 |
| 11-14 16:01 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 16:01 | +20 | HYPE | DOWN | 0.57 | 0.77 | 1.69 |
| 11-14 16:01 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-14 16:01 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 16:01 | +5 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 16:01 | +10 stop | BTC | DOWN | 0.46 | 0.56 | 0.64 |
| 11-14 16:01 | +20 | BTC | DOWN | 0.47 | 0.82 | 3.21 |
| 11-14 16:01 | +15 | BTC | DOWN | 0.47 | 0.62 | 1.15 |
| 11-14 16:01 | +10 | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 11-14 16:01 | +5 | BTC | DOWN | 0.47 | 0.55 | 0.44 |
| 11-14 16:01 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-14 16:01 | +20 | DOGE | DOWN | 0.67 | 0.89 | 1.97 |
| 11-14 16:01 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-14 16:01 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-14 16:01 | +5 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-14 16:01 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-14 16:01 | +20 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
