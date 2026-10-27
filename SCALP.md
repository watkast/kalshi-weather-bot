# Range-Scalp Bot

*Updated Tue Oct 27 18:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36921 | 32244 | 4677 (44) | 4 | $-10200.01 | -4.4% |
| **+10¢** | 27579 | 22162 | 5417 (66) | 4 | $-9058.72 | -5.2% |
| **+15¢** | 23075 | 17261 | 5814 (90) | 4 | $-7981.39 | -5.5% |
| **+20¢** | 20452 | 14366 | 6086 (115) | 5 | $-6947.92 | -5.4% |
| **+10¢ (15¢ stop)** | 45229 | 45165 | 64 (33) | 2 | $-17221.56 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 18:39 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-27 18:39 | +10 stop | ETH | UP | 0.61 | 0.37 | -2.73 |
| 10-27 18:38 | +5 | ETH | UP | 0.69 | open |  |
| 10-27 18:37 | +10 stop | ETH | UP | 0.59 | 0.72 | 0.98 |
| 10-27 18:37 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 10-27 18:37 | +10 stop | NEAR | UP | 0.58 | 0.39 | -2.25 |
| 10-27 18:36 | +10 stop | BTC | UP | 0.67 | open |  |
| 10-27 18:36 | +10 stop | ETH | DOWN | 0.55 | 0.27 | -3.12 |
| 10-27 18:36 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-27 18:36 | +15 | ETH | DOWN | 0.55 | 0.70 | 1.17 |
| 10-27 18:36 | +10 | ETH | DOWN | 0.55 | 0.70 | 1.17 |
| 10-27 18:36 | +5 | ETH | DOWN | 0.55 | 0.62 | 0.35 |
| 10-27 18:35 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-27 18:35 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-27 18:35 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-27 18:35 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 18:35 | +10 stop | ZEC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-27 18:35 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-27 18:35 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-27 18:35 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-27 18:34 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-27 18:34 | +10 stop | BTC | DOWN | 0.69 | 0.52 | -2.03 |
| 10-27 18:34 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-27 18:34 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-27 18:33 | +10 stop | XRP | UP | 0.61 | 0.71 | 0.68 |
| 10-27 18:33 | +5 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-27 18:33 | +10 stop | SOL | DOWN | 0.65 | 0.46 | -2.24 |
| 10-27 18:33 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-27 18:33 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-27 18:33 | +5 | SOL | DOWN | 0.64 | open |  |
| 10-27 18:33 | +10 stop | NEAR | DOWN | 0.67 | 0.52 | -1.84 |
| 10-27 18:33 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-27 18:33 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 18:33 | +10 stop | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 10-27 18:33 | +10 stop | HYPE | DOWN | 0.50 | 0.30 | -2.33 |
| 10-27 18:33 | +10 stop | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 10-27 18:32 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-27 18:32 | +10 stop | XRP | DOWN | 0.59 | 0.42 | -2.05 |
| 10-27 18:32 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-27 18:32 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
