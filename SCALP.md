# Range-Scalp Bot

*Updated Sat Nov 14 12:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59471 | 51893 | 7578 (107) | 2 | $-16053.59 | -4.3% |
| **+10¢** | 44416 | 35546 | 8870 (142) | 2 | $-15066.46 | -5.4% |
| **+15¢** | 37223 | 27657 | 9566 (178) | 2 | $-13705.73 | -5.9% |
| **+20¢** | 33157 | 23117 | 10040 (230) | 2 | $-12079.67 | -5.8% |
| **+10¢ (15¢ stop)** | 72352 | 72210 | 142 (82) | 0 | $-26604.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 12:27 | +10 stop | BNB | DOWN | 0.56 | 0.15 | -4.37 |
| 11-14 12:27 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-14 12:27 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-14 12:27 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-14 12:27 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-14 12:27 | +10 stop | SOL | UP | 0.51 | 0.75 | 2.08 |
| 11-14 12:27 | +10 | SOL | UP | 0.51 | 0.75 | 2.08 |
| 11-14 12:27 | +5 | SOL | UP | 0.50 | 0.57 | 0.34 |
| 11-14 12:25 | +10 stop | DOGE | DOWN | 0.57 | 0.83 | 2.32 |
| 11-14 12:25 | +20 | DOGE | DOWN | 0.56 | 0.83 | 2.42 |
| 11-14 12:25 | +15 | DOGE | DOWN | 0.56 | 0.83 | 2.42 |
| 11-14 12:25 | +10 | DOGE | DOWN | 0.56 | 0.83 | 2.42 |
| 11-14 12:25 | +5 | DOGE | DOWN | 0.56 | 0.65 | 0.56 |
| 11-14 12:25 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.89 |
| 11-14 12:25 | +20 | ETH | DOWN | 0.57 | 0.78 | 1.79 |
| 11-14 12:25 | +15 | ETH | DOWN | 0.57 | 0.78 | 1.79 |
| 11-14 12:25 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-14 12:25 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 11-14 12:24 | +10 stop | NEAR | UP | 0.63 | 0.77 | 1.10 |
| 11-14 12:24 | +10 stop | SOL | DOWN | 0.66 | 0.48 | -2.14 |
| 11-14 12:24 | +10 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-14 12:24 | +5 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 11-14 12:21 | +10 stop | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-14 12:20 | +10 stop | SOL | UP | 0.55 | 0.30 | -2.83 |
| 11-14 12:20 | +10 stop | XRP | DOWN | 0.63 | 0.74 | 0.80 |
| 11-14 12:20 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-14 12:20 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-14 12:20 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-14 12:20 | +15 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 11-14 12:20 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-14 12:20 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 11-14 12:20 | +10 stop | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-14 12:20 | +20 | BTC | DOWN | 0.65 | 0.89 | 2.17 |
| 11-14 12:20 | +15 | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 11-14 12:20 | +10 | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-14 12:20 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-14 12:20 | +10 stop | ZEC | DOWN | 0.46 | 0.61 | 1.15 |
| 11-14 12:20 | +20 | ZEC | DOWN | 0.46 | 0.67 | 1.76 |
| 11-14 12:20 | +15 | ZEC | DOWN | 0.46 | 0.61 | 1.15 |
| 11-14 12:20 | +10 | ZEC | DOWN | 0.46 | 0.61 | 1.15 |
