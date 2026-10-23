# Range-Scalp Bot

*Updated Fri Oct 23 13:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30409 | 26489 | 3920 (39) | 8 | $-8861.11 | -4.6% |
| **+10¢** | 22769 | 18233 | 4536 (56) | 9 | $-7934.35 | -5.5% |
| **+15¢** | 19056 | 14177 | 4879 (79) | 9 | $-7168.94 | -6.0% |
| **+20¢** | 16873 | 11761 | 5112 (102) | 9 | $-6453.56 | -6.1% |
| **+10¢ (15¢ stop)** | 37281 | 37222 | 59 (32) | 7 | $-14086.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 13:38 | +5 | DOGE | UP | 0.54 | 0.59 | 0.15 |
| 10-23 13:38 | +10 stop | SOL | UP | 0.59 | open |  |
| 10-23 13:38 | +10 | SOL | UP | 0.59 | open |  |
| 10-23 13:38 | +5 | SOL | UP | 0.59 | open |  |
| 10-23 13:38 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 10-23 13:38 | +5 | HYPE | DOWN | 0.55 | open |  |
| 10-23 13:38 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 10-23 13:38 | +10 stop | ETH | UP | 0.55 | open |  |
| 10-23 13:38 | +5 | ETH | UP | 0.55 | open |  |
| 10-23 13:38 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 10-23 13:38 | +10 stop | DOGE | UP | 0.63 | open |  |
| 10-23 13:38 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 10-23 13:38 | +10 stop | BNB | DOWN | 0.57 | 0.68 | 0.76 |
| 10-23 13:38 | +10 stop | DOGE | DOWN | 0.45 | 0.55 | 0.64 |
| 10-23 13:37 | +10 stop | BTC | DOWN | 0.44 | 0.60 | 1.25 |
| 10-23 13:37 | +5 | ETH | DOWN | 0.46 | 0.66 | 1.66 |
| 10-23 13:37 | +10 stop | DOGE | DOWN | 0.50 | 0.64 | 1.05 |
| 10-23 13:36 | +10 stop | XRP | DOWN | 0.54 | 0.70 | 1.27 |
| 10-23 13:36 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.67 |
| 10-23 13:36 | +5 | SOL | UP | 0.61 | 0.69 | 0.48 |
| 10-23 13:36 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 10-23 13:36 | +5 | ETH | UP | 0.51 | 0.56 | 0.14 |
| 10-23 13:36 | +10 stop | SOL | UP | 0.56 | 0.69 | 0.97 |
| 10-23 13:36 | +10 | SOL | UP | 0.57 | 0.69 | 0.87 |
| 10-23 13:35 | +10 stop | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-23 13:35 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 10-23 13:35 | +5 | DOGE | UP | 0.55 | 0.63 | 0.45 |
| 10-23 13:35 | +5 | ETH | UP | 0.55 | 0.65 | 0.66 |
| 10-23 13:35 | +10 stop | ETH | UP | 0.66 | 0.45 | -2.44 |
| 10-23 13:35 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 10-23 13:35 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 10-23 13:35 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 10-23 13:34 | +10 stop | BNB | UP | 0.55 | 0.38 | -2.05 |
| 10-23 13:34 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-23 13:34 | +10 stop | NEAR | UP | 0.60 | 0.43 | -2.05 |
| 10-23 13:34 | +5 | HYPE | DOWN | 0.53 | 0.58 | 0.14 |
| 10-23 13:33 | +10 stop | ZEC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-23 13:32 | +5 | HYPE | DOWN | 0.47 | 0.56 | 0.54 |
| 10-23 13:32 | +10 stop | ZEC | UP | 0.49 | 0.34 | -1.84 |
| 10-23 13:32 | +10 stop | HYPE | UP | 0.49 | 0.23 | -2.91 |
