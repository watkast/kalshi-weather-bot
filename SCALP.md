# Range-Scalp Bot

*Updated Mon Oct 05 11:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3747 | 3227 | 520 (3) | 2 | $-1289.30 | -5.4% |
| **+10¢** | 2902 | 2304 | 598 (4) | 2 | $-1157.80 | -6.3% |
| **+15¢** | 2438 | 1809 | 629 (7) | 2 | $-984.58 | -6.4% |
| **+20¢** | 2178 | 1523 | 655 (12) | 2 | $-813.23 | -5.9% |
| **+10¢ (15¢ stop)** | 4639 | 4638 | 1 (1) | 0 | $-1744.86 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 11:37 | +10 stop | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-05 11:34 | +10 stop | BNB | UP | 0.55 | 0.39 | -1.94 |
| 10-05 11:34 | +20 | BNB | UP | 0.55 | open |  |
| 10-05 11:34 | +15 | BNB | UP | 0.54 | open |  |
| 10-05 11:34 | +10 | BNB | UP | 0.55 | open |  |
| 10-05 11:34 | +5 | BNB | UP | 0.54 | open |  |
| 10-05 11:33 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 11:33 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 11:33 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-05 11:33 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.95 |
| 10-05 11:33 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-05 11:33 | +20 | BTC | DOWN | 0.71 | 0.93 | 1.99 |
| 10-05 11:33 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.33 |
| 10-05 11:33 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-05 11:33 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-05 11:32 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.51 |
| 10-05 11:31 | +10 stop | ZEC | UP | 0.61 | 0.45 | -2.00 |
| 10-05 11:31 | +20 | ZEC | UP | 0.62 | 0.93 | 2.84 |
| 10-05 11:31 | +15 | ZEC | UP | 0.62 | 0.93 | 2.84 |
| 10-05 11:31 | +10 | ZEC | UP | 0.62 | 0.93 | 2.84 |
| 10-05 11:31 | +5 | ZEC | UP | 0.62 | 0.93 | 2.84 |
| 10-05 11:31 | +10 stop | DOGE | DOWN | 0.55 | 0.67 | 0.89 |
| 10-05 11:31 | +20 | DOGE | DOWN | 0.55 | 0.75 | 1.71 |
| 10-05 11:31 | +15 | DOGE | DOWN | 0.55 | 0.75 | 1.71 |
| 10-05 11:31 | +10 | DOGE | DOWN | 0.55 | 0.67 | 0.89 |
| 10-05 11:31 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.38 |
| 10-05 11:31 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-05 11:31 | +20 | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 10-05 11:31 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-05 11:31 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-05 11:31 | +5 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-05 11:31 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 11:31 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-05 11:31 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 10-05 11:31 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 11:31 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-05 11:31 | +10 stop | SOL | DOWN | 0.61 | 0.72 | 0.78 |
| 10-05 11:31 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 11:31 | +15 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 10-05 11:31 | +10 | SOL | DOWN | 0.61 | 0.72 | 0.78 |
