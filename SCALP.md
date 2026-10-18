# Range-Scalp Bot

*Updated Sun Oct 18 23:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23111 | 20088 | 3023 (30) | 2 | $-6947.62 | -4.8% |
| **+10¢** | 17378 | 13890 | 3488 (44) | 3 | $-6241.50 | -5.7% |
| **+15¢** | 14573 | 10813 | 3760 (66) | 3 | $-5685.56 | -6.2% |
| **+20¢** | 12906 | 8974 | 3932 (84) | 4 | $-5065.09 | -6.3% |
| **+10¢ (15¢ stop)** | 28443 | 28392 | 51 (30) | 3 | $-10870.46 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 23:37 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-18 23:37 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-18 23:37 | +5 | DOGE | DOWN | 0.69 | 0.75 | 0.31 |
| 10-18 23:37 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 10-18 23:37 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-18 23:37 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-18 23:37 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-18 23:35 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-18 23:35 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-18 23:35 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-18 23:35 | +5 | DOGE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-18 23:35 | +10 stop | BTC | DOWN | 0.56 | open |  |
| 10-18 23:35 | +10 | BTC | DOWN | 0.56 | open |  |
| 10-18 23:35 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-18 23:35 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-18 23:35 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 10-18 23:35 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-18 23:35 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-18 23:35 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-18 23:35 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-18 23:35 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-18 23:34 | +10 stop | NEAR | DOWN | 0.54 | 0.69 | 1.21 |
| 10-18 23:34 | +15 | NEAR | DOWN | 0.54 | 0.69 | 1.21 |
| 10-18 23:34 | +10 | NEAR | DOWN | 0.54 | 0.69 | 1.21 |
| 10-18 23:34 | +5 | NEAR | DOWN | 0.54 | 0.69 | 1.21 |
| 10-18 23:34 | +10 stop | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 10-18 23:34 | +15 | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
| 10-18 23:34 | +10 | DOGE | DOWN | 0.45 | 0.61 | 1.25 |
| 10-18 23:34 | +5 | DOGE | DOWN | 0.45 | 0.61 | 1.25 |
| 10-18 23:34 | +10 stop | BTC | DOWN | 0.45 | 0.55 | 0.64 |
| 10-18 23:34 | +10 | BTC | DOWN | 0.43 | 0.55 | 0.84 |
| 10-18 23:34 | +5 | BTC | DOWN | 0.43 | 0.55 | 0.84 |
| 10-18 23:32 | +10 stop | DOGE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-18 23:32 | +20 | DOGE | DOWN | 0.63 | open |  |
| 10-18 23:32 | +15 | DOGE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-18 23:32 | +10 | DOGE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-18 23:32 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-18 23:32 | +10 stop | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-18 23:32 | +20 | SOL | DOWN | 0.61 | 0.83 | 1.93 |
| 10-18 23:32 | +15 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
