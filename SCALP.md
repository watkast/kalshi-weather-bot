# Range-Scalp Bot

*Updated Sun Nov 01 16:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43656 | 38040 | 5616 (64) | 0 | $-12459.76 | -4.5% |
| **+10¢** | 32570 | 26086 | 6484 (85) | 4 | $-11165.62 | -5.5% |
| **+15¢** | 27261 | 20277 | 6984 (112) | 4 | $-10202.47 | -6.0% |
| **+20¢** | 24203 | 16888 | 7315 (146) | 6 | $-9011.03 | -5.9% |
| **+10¢ (15¢ stop)** | 53256 | 53170 | 86 (51) | 3 | $-20107.61 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 16:09 | +5 | NEAR | UP | 0.55 | 0.65 | 0.66 |
| 11-01 16:09 | +10 stop | BTC | UP | 0.57 | open |  |
| 11-01 16:09 | +10 | BTC | UP | 0.57 | open |  |
| 11-01 16:09 | +5 | BTC | UP | 0.56 | 0.62 | 0.25 |
| 11-01 16:09 | +5 | ETH | UP | 0.52 | 0.69 | 1.37 |
| 11-01 16:09 | +10 stop | SOL | UP | 0.50 | 0.66 | 1.26 |
| 11-01 16:09 | +15 | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-01 16:09 | +10 | SOL | UP | 0.52 | 0.66 | 1.06 |
| 11-01 16:09 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-01 16:08 | +10 stop | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-01 16:08 | +15 | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-01 16:08 | +10 | SOL | UP | 0.51 | 0.66 | 1.16 |
| 11-01 16:08 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 11-01 16:07 | +10 stop | BNB | DOWN | 0.61 | 0.78 | 1.35 |
| 11-01 16:07 | +15 | BNB | DOWN | 0.60 | 0.78 | 1.45 |
| 11-01 16:07 | +10 | BNB | DOWN | 0.60 | 0.78 | 1.45 |
| 11-01 16:07 | +5 | BNB | DOWN | 0.60 | 0.69 | 0.53 |
| 11-01 16:06 | +10 stop | NEAR | UP | 0.69 | open |  |
| 11-01 16:06 | +5 | NEAR | UP | 0.69 | 0.75 | 0.31 |
| 11-01 16:06 | +10 stop | ETH | UP | 0.70 | open |  |
| 11-01 16:06 | +5 | ETH | UP | 0.70 | 0.77 | 0.42 |
| 11-01 16:04 | +10 stop | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 11-01 16:04 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-01 16:04 | +10 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-01 16:04 | +5 | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-01 16:04 | +10 stop | XRP | UP | 0.60 | 0.81 | 1.82 |
| 11-01 16:04 | +10 stop | SOL | UP | 0.50 | 0.71 | 1.77 |
| 11-01 16:04 | +20 | SOL | UP | 0.56 | open |  |
| 11-01 16:04 | +15 | SOL | UP | 0.56 | 0.71 | 1.17 |
| 11-01 16:04 | +10 | SOL | UP | 0.56 | 0.71 | 1.17 |
| 11-01 16:04 | +5 | SOL | UP | 0.56 | 0.71 | 1.17 |
| 11-01 16:04 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-01 16:04 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-01 16:03 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-01 16:02 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-01 16:02 | +10 stop | NEAR | DOWN | 0.60 | 0.42 | -2.15 |
| 11-01 16:02 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 11-01 16:02 | +15 | BNB | DOWN | 0.57 | 0.78 | 1.79 |
| 11-01 16:02 | +10 | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 11-01 16:02 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
