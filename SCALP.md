# Range-Scalp Bot

*Updated Wed Oct 21 23:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27924 | 24329 | 3595 (39) | 6 | $-8037.71 | -4.6% |
| **+10¢** | 20982 | 16831 | 4151 (55) | 6 | $-7072.87 | -5.4% |
| **+15¢** | 17574 | 13106 | 4468 (78) | 6 | $-6311.26 | -5.7% |
| **+20¢** | 15555 | 10873 | 4682 (98) | 8 | $-5643.48 | -5.8% |
| **+10¢ (15¢ stop)** | 34285 | 34226 | 59 (32) | 3 | $-12795.42 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 23:55 | +5 | SOL | DOWN | 0.62 | open |  |
| 10-21 23:54 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-21 23:54 | +10 stop | DOGE | UP | 0.60 | open |  |
| 10-21 23:54 | +10 | DOGE | UP | 0.60 | open |  |
| 10-21 23:54 | +5 | DOGE | UP | 0.60 | open |  |
| 10-21 23:54 | +10 stop | SOL | UP | 0.49 | open |  |
| 10-21 23:54 | +20 | SOL | UP | 0.49 | open |  |
| 10-21 23:54 | +15 | SOL | UP | 0.49 | open |  |
| 10-21 23:54 | +10 | SOL | UP | 0.49 | open |  |
| 10-21 23:54 | +5 | SOL | UP | 0.49 | 0.54 | 0.14 |
| 10-21 23:53 | +10 stop | ZEC | DOWN | 0.54 | open |  |
| 10-21 23:53 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-21 23:53 | +5 | ZEC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-21 23:52 | +10 stop | NEAR | DOWN | 0.53 | 0.31 | -2.53 |
| 10-21 23:52 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-21 23:52 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-21 23:52 | +15 | ZEC | DOWN | 0.69 | open |  |
| 10-21 23:52 | +10 | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-21 23:52 | +5 | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-21 23:51 | +10 stop | NEAR | DOWN | 0.71 | 0.56 | -1.83 |
| 10-21 23:51 | +15 | NEAR | DOWN | 0.71 | open |  |
| 10-21 23:51 | +10 | NEAR | DOWN | 0.71 | open |  |
| 10-21 23:51 | +5 | NEAR | DOWN | 0.71 | open |  |
| 10-21 23:50 | +10 stop | DOGE | DOWN | 0.65 | 0.34 | -3.42 |
| 10-21 23:50 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 10-21 23:49 | +10 stop | ZEC | DOWN | 0.60 | 0.72 | 0.88 |
| 10-21 23:49 | +10 | ZEC | DOWN | 0.59 | 0.72 | 0.95 |
| 10-21 23:49 | +10 stop | XRP | DOWN | 0.53 | 0.70 | 1.37 |
| 10-21 23:49 | +5 | NEAR | DOWN | 0.60 | 0.69 | 0.58 |
| 10-21 23:49 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-21 23:49 | +10 stop | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-21 23:49 | +15 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 10-21 23:49 | +10 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 10-21 23:49 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-21 23:49 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 10-21 23:49 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-21 23:49 | +5 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-21 23:48 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-21 23:48 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-21 23:48 | +5 | XRP | UP | 0.52 | 0.59 | 0.35 |
