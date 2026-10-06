# Range-Scalp Bot

*Updated Tue Oct 06 10:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4959 | 4289 | 670 (7) | 5 | $-1586.12 | -5.1% |
| **+10¢** | 3802 | 3022 | 780 (11) | 7 | $-1460.71 | -6.1% |
| **+15¢** | 3196 | 2369 | 827 (14) | 6 | $-1264.51 | -6.3% |
| **+20¢** | 2862 | 1999 | 863 (19) | 7 | $-1048.55 | -5.8% |
| **+10¢ (15¢ stop)** | 6068 | 6055 | 13 (8) | 4 | $-2179.91 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 10:53 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-06 10:52 | +10 stop | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 10-06 10:52 | +10 stop | SOL | DOWN | 0.61 | open |  |
| 10-06 10:52 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-06 10:52 | +15 | SOL | DOWN | 0.61 | open |  |
| 10-06 10:52 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-06 10:52 | +5 | SOL | DOWN | 0.61 | open |  |
| 10-06 10:52 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 10-06 10:52 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-06 10:52 | +10 | XRP | DOWN | 0.62 | open |  |
| 10-06 10:52 | +5 | XRP | DOWN | 0.62 | open |  |
| 10-06 10:52 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-06 10:52 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-06 10:52 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-06 10:52 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-06 10:51 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-06 10:51 | +10 stop | DOGE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-06 10:50 | +10 stop | ZEC | UP | 0.52 | 0.34 | -2.14 |
| 10-06 10:50 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-06 10:50 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-06 10:49 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 10-06 10:49 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-06 10:49 | +10 stop | ZEC | DOWN | 0.61 | 0.45 | -1.94 |
| 10-06 10:49 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.21 |
| 10-06 10:49 | +10 | ZEC | DOWN | 0.60 | 0.70 | 0.69 |
| 10-06 10:49 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.38 |
| 10-06 10:47 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-06 10:47 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-06 10:47 | +5 | DOGE | DOWN | 0.69 | open |  |
| 10-06 10:47 | +10 stop | BTC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-06 10:47 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-06 10:47 | +10 stop | HYPE | DOWN | 0.65 | 0.49 | -1.98 |
| 10-06 10:47 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.24 |
| 10-06 10:47 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 10-06 10:47 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.94 |
| 10-06 10:47 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-06 10:47 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-06 10:47 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-06 10:47 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 10-06 10:46 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
