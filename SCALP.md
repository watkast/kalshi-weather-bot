# Range-Scalp Bot

*Updated Sun Nov 22 10:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68476 | 59744 | 8732 (142) | 2 | $-18460.85 | -4.3% |
| **+10¢** | 51135 | 40934 | 10201 (186) | 5 | $-17144.57 | -5.3% |
| **+15¢** | 42857 | 31863 | 10994 (237) | 6 | $-15379.45 | -5.7% |
| **+20¢** | 38155 | 26602 | 11553 (295) | 6 | $-13706.97 | -5.7% |
| **+10¢ (15¢ stop)** | 83409 | 83224 | 185 (116) | 4 | $-30682.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 10:31 | +10 stop | ETH | DOWN | 0.56 | open |  |
| 11-22 10:31 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-22 10:31 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-22 10:31 | +10 | ETH | DOWN | 0.55 | open |  |
| 11-22 10:31 | +5 | ETH | DOWN | 0.56 | 0.62 | 0.25 |
| 11-22 10:31 | +10 stop | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-22 10:31 | +20 | XRP | DOWN | 0.51 | open |  |
| 11-22 10:31 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-22 10:31 | +10 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-22 10:31 | +5 | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 11-22 10:31 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 11-22 10:31 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-22 10:31 | +15 | SOL | DOWN | 0.66 | open |  |
| 11-22 10:31 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-22 10:31 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-22 10:31 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-22 10:31 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-22 10:31 | +15 | BNB | DOWN | 0.70 | open |  |
| 11-22 10:31 | +10 | BNB | DOWN | 0.70 | open |  |
| 11-22 10:31 | +5 | BNB | DOWN | 0.70 | open |  |
| 11-22 10:30 | +10 stop | ZEC | DOWN | 0.69 | open |  |
| 11-22 10:30 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-22 10:30 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-22 10:30 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-22 10:30 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-22 10:30 | +10 stop | NEAR | DOWN | 0.64 | 0.46 | -2.15 |
| 11-22 10:30 | +20 | NEAR | DOWN | 0.63 | open |  |
| 11-22 10:30 | +15 | NEAR | DOWN | 0.63 | open |  |
| 11-22 10:30 | +10 | NEAR | DOWN | 0.61 | open |  |
| 11-22 10:30 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-22 10:28 | +10 stop | XRP | UP | 0.29 | 0.59 | 2.68 |
| 11-22 10:28 | +20 | XRP | UP | 0.35 | 0.59 | 2.10 |
| 11-22 10:28 | +15 | XRP | UP | 0.34 | 0.59 | 2.14 |
| 11-22 10:28 | +10 | XRP | UP | 0.35 | 0.59 | 2.04 |
| 11-22 10:28 | +5 | XRP | UP | 0.36 | 0.59 | 1.96 |
| 11-22 10:27 | +10 stop | ZEC | UP | 0.52 | 0.65 | 0.96 |
| 11-22 10:26 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-22 10:26 | +20 | DOGE | DOWN | 0.69 | 1.00 | 2.90 |
| 11-22 10:26 | +15 | DOGE | DOWN | 0.70 | 1.00 | 2.80 |
| 11-22 10:26 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
