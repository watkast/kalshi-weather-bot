# Range-Scalp Bot

*Updated Sun Nov 22 19:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69028 | 60238 | 8790 (145) | 5 | $-18534.63 | -4.3% |
| **+10¢** | 51512 | 41248 | 10264 (188) | 5 | $-17169.09 | -5.3% |
| **+15¢** | 43170 | 32105 | 11065 (240) | 5 | $-15405.61 | -5.7% |
| **+20¢** | 38440 | 26813 | 11627 (299) | 5 | $-13691.77 | -5.7% |
| **+10¢ (15¢ stop)** | 84055 | 83866 | 189 (117) | 1 | $-30938.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 19:57 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-22 19:57 | +10 | ETH | UP | 0.63 | open |  |
| 11-22 19:57 | +5 | ETH | UP | 0.66 | open |  |
| 11-22 19:54 | +10 stop | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-22 19:54 | +5 | NEAR | DOWN | 0.66 | 0.85 | 1.65 |
| 11-22 19:53 | +10 stop | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 11-22 19:53 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.79 |
| 11-22 19:53 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-22 19:53 | +10 | NEAR | DOWN | 0.71 | 0.85 | 1.16 |
| 11-22 19:52 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.02 |
| 11-22 19:52 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-22 19:51 | +10 stop | ETH | UP | 0.57 | 0.76 | 1.59 |
| 11-22 19:51 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-22 19:51 | +20 | XRP | UP | 0.59 | 0.80 | 1.81 |
| 11-22 19:51 | +15 | XRP | UP | 0.59 | 0.77 | 1.50 |
| 11-22 19:51 | +10 | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-22 19:51 | +5 | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-22 19:51 | +10 stop | BNB | DOWN | 0.61 | 0.85 | 2.14 |
| 11-22 19:50 | +10 stop | BTC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-22 19:50 | +10 stop | HYPE | UP | 0.50 | 0.68 | 1.46 |
| 11-22 19:49 | +10 stop | BNB | DOWN | 0.56 | 0.70 | 1.07 |
| 11-22 19:49 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.81 |
| 11-22 19:49 | +10 stop | ZEC | DOWN | 0.57 | 0.69 | 0.87 |
| 11-22 19:49 | +10 stop | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 19:49 | +10 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 19:49 | +5 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-22 19:48 | +10 stop | ETH | UP | 0.61 | 0.46 | -1.85 |
| 11-22 19:48 | +10 | ETH | UP | 0.62 | 0.76 | 1.10 |
| 11-22 19:48 | +5 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-22 19:48 | +10 stop | BTC | UP | 0.52 | 0.32 | -2.34 |
| 11-22 19:48 | +20 | BTC | UP | 0.52 | open |  |
| 11-22 19:48 | +15 | BTC | UP | 0.52 | open |  |
| 11-22 19:48 | +10 | BTC | UP | 0.52 | open |  |
| 11-22 19:48 | +5 | BTC | UP | 0.52 | open |  |
| 11-22 19:48 | +10 stop | BNB | UP | 0.63 | 0.38 | -2.84 |
| 11-22 19:48 | +20 | BNB | UP | 0.63 | open |  |
| 11-22 19:48 | +15 | BNB | UP | 0.63 | open |  |
| 11-22 19:48 | +10 | BNB | UP | 0.63 | open |  |
| 11-22 19:48 | +5 | BNB | UP | 0.63 | open |  |
| 11-22 19:47 | +10 stop | ZEC | UP | 0.53 | 0.37 | -1.95 |
