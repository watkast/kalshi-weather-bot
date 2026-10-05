# Range-Scalp Bot

*Updated Mon Oct 05 11:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3761 | 3239 | 522 (3) | 7 | $-1294.29 | -5.5% |
| **+10¢** | 2908 | 2308 | 600 (4) | 8 | $-1165.11 | -6.4% |
| **+15¢** | 2442 | 1811 | 631 (7) | 7 | $-992.90 | -6.5% |
| **+20¢** | 2180 | 1523 | 657 (12) | 9 | $-824.18 | -6.0% |
| **+10¢ (15¢ stop)** | 4658 | 4657 | 1 (1) | 2 | $-1756.59 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 11:54 | +10 stop | BNB | DOWN | 0.66 | 0.50 | -1.94 |
| 10-05 11:53 | +10 stop | XRP | UP | 0.58 | 0.80 | 1.86 |
| 10-05 11:53 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-05 11:53 | +10 stop | ETH | DOWN | 0.67 | open |  |
| 10-05 11:53 | +10 | ETH | DOWN | 0.67 | open |  |
| 10-05 11:53 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-05 11:53 | +10 stop | ZEC | UP | 0.63 | open |  |
| 10-05 11:53 | +10 | ZEC | UP | 0.63 | open |  |
| 10-05 11:53 | +5 | ZEC | UP | 0.63 | open |  |
| 10-05 11:53 | +10 stop | NEAR | DOWN | 0.57 | 0.31 | -2.94 |
| 10-05 11:53 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.24 |
| 10-05 11:52 | +10 stop | NEAR | DOWN | 0.53 | 0.64 | 0.76 |
| 10-05 11:52 | +5 | NEAR | DOWN | 0.53 | 0.64 | 0.76 |
| 10-05 11:52 | +5 | BNB | DOWN | 0.70 | open |  |
| 10-05 11:52 | +10 stop | XRP | DOWN | 0.52 | 0.34 | -2.14 |
| 10-05 11:50 | +10 stop | XRP | UP | 0.63 | 0.44 | -2.25 |
| 10-05 11:49 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-05 11:49 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-05 11:49 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-05 11:49 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-05 11:49 | +5 | ZEC | DOWN | 0.60 | 0.69 | 0.58 |
| 10-05 11:49 | +10 stop | SOL | UP | 0.64 | 0.81 | 1.42 |
| 10-05 11:48 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-05 11:47 | +10 stop | NEAR | UP | 0.55 | 0.76 | 1.79 |
| 10-05 11:47 | +5 | HYPE | DOWN | 0.59 | open |  |
| 10-05 11:47 | +5 | NEAR | UP | 0.60 | 0.76 | 1.30 |
| 10-05 11:47 | +10 stop | XRP | DOWN | 0.53 | 0.38 | -1.85 |
| 10-05 11:47 | +10 | XRP | DOWN | 0.53 | open |  |
| 10-05 11:47 | +5 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-05 11:47 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-05 11:47 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 10-05 11:47 | +20 | DOGE | DOWN | 0.55 | open |  |
| 10-05 11:47 | +15 | DOGE | DOWN | 0.55 | open |  |
| 10-05 11:47 | +10 | DOGE | DOWN | 0.55 | open |  |
| 10-05 11:47 | +5 | DOGE | DOWN | 0.55 | open |  |
| 10-05 11:47 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-05 11:47 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-05 11:47 | +15 | ETH | DOWN | 0.59 | 0.75 | 1.30 |
| 10-05 11:47 | +10 | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-05 11:47 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
