# Range-Scalp Bot

*Updated Sun Nov 22 10:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68488 | 59756 | 8732 (142) | 2 | $-18454.41 | -4.3% |
| **+10¢** | 51145 | 40944 | 10201 (186) | 3 | $-17135.30 | -5.3% |
| **+15¢** | 42865 | 31871 | 10994 (237) | 3 | $-15368.17 | -5.7% |
| **+20¢** | 38161 | 26608 | 11553 (295) | 5 | $-13696.05 | -5.7% |
| **+10¢ (15¢ stop)** | 83426 | 83241 | 185 (116) | 1 | $-30686.81 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 10:41 | +10 stop | NEAR | UP | 0.67 | open |  |
| 11-22 10:41 | +20 | NEAR | UP | 0.67 | open |  |
| 11-22 10:41 | +15 | NEAR | UP | 0.67 | open |  |
| 11-22 10:41 | +10 | NEAR | UP | 0.67 | open |  |
| 11-22 10:41 | +5 | NEAR | UP | 0.67 | 0.75 | 0.50 |
| 11-22 10:40 | +10 stop | ETH | DOWN | 0.62 | 0.37 | -2.84 |
| 11-22 10:38 | +10 stop | ETH | DOWN | 0.63 | 0.45 | -2.15 |
| 11-22 10:38 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-22 10:38 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-22 10:38 | +10 | ETH | DOWN | 0.63 | open |  |
| 11-22 10:38 | +5 | ETH | DOWN | 0.63 | open |  |
| 11-22 10:37 | +10 stop | XRP | DOWN | 0.60 | 0.45 | -1.85 |
| 11-22 10:36 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 11-22 10:36 | +5 | NEAR | DOWN | 0.62 | 0.69 | 0.38 |
| 11-22 10:35 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-22 10:35 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 10:35 | +5 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 10:35 | +5 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-22 10:35 | +10 stop | NEAR | UP | 0.69 | 0.37 | -3.52 |
| 11-22 10:35 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.95 |
| 11-22 10:35 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.95 |
| 11-22 10:35 | +5 | HYPE | DOWN | 0.69 | 0.78 | 0.63 |
| 11-22 10:35 | +10 stop | XRP | DOWN | 0.51 | 0.65 | 1.06 |
| 11-22 10:33 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 10:33 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-22 10:33 | +15 | DOGE | DOWN | 0.70 | 0.85 | 1.26 |
| 11-22 10:33 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 10:33 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-22 10:33 | +10 stop | XRP | DOWN | 0.69 | 0.47 | -2.53 |
| 11-22 10:33 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-22 10:33 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-22 10:32 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 11-22 10:32 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-22 10:32 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-22 10:32 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-22 10:32 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-22 10:32 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-22 10:32 | +10 stop | NEAR | DOWN | 0.57 | 0.39 | -2.15 |
| 11-22 10:32 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 11-22 10:32 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
