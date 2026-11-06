# Range-Scalp Bot

*Updated Fri Nov 06 22:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50070 | 43647 | 6423 (76) | 4 | $-14057.54 | -4.5% |
| **+10¢** | 37371 | 29898 | 7473 (102) | 4 | $-12951.26 | -5.5% |
| **+15¢** | 31298 | 23243 | 8055 (131) | 5 | $-11873.49 | -6.0% |
| **+20¢** | 27826 | 19381 | 8445 (172) | 4 | $-10498.49 | -6.0% |
| **+10¢ (15¢ stop)** | 60990 | 60891 | 99 (58) | 4 | $-22609.64 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 22:36 | +10 stop | SOL | DOWN | 0.67 | open |  |
| 11-06 22:36 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-06 22:36 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 11-06 22:35 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-06 22:35 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-06 22:35 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-06 22:35 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-06 22:35 | +5 | ETH | UP | 0.54 | open |  |
| 11-06 22:35 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.25 |
| 11-06 22:35 | +10 stop | DOGE | DOWN | 0.66 | 0.45 | -2.44 |
| 11-06 22:34 | +10 stop | HYPE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-06 22:34 | +5 | SOL | UP | 0.54 | open |  |
| 11-06 22:33 | +10 stop | HYPE | DOWN | 0.65 | 0.46 | -2.24 |
| 11-06 22:33 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 22:32 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 22:32 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-06 22:32 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-06 22:32 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 22:32 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-06 22:32 | +10 stop | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 22:32 | +20 | BTC | DOWN | 0.57 | 0.78 | 1.79 |
| 11-06 22:32 | +15 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 22:32 | +10 | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 22:32 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-06 22:32 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-06 22:32 | +10 stop | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-06 22:32 | +10 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-06 22:32 | +5 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-06 22:31 | +10 stop | BNB | UP | 0.65 | 0.46 | -2.24 |
| 11-06 22:31 | +20 | BNB | UP | 0.65 | open |  |
| 11-06 22:31 | +15 | BNB | UP | 0.65 | open |  |
| 11-06 22:31 | +10 | BNB | UP | 0.65 | open |  |
| 11-06 22:31 | +5 | BNB | UP | 0.65 | open |  |
| 11-06 22:31 | +10 stop | DOGE | UP | 0.55 | 0.36 | -2.25 |
| 11-06 22:31 | +20 | DOGE | UP | 0.55 | open |  |
| 11-06 22:31 | +15 | DOGE | UP | 0.55 | open |  |
| 11-06 22:31 | +10 | DOGE | UP | 0.55 | open |  |
| 11-06 22:31 | +5 | DOGE | UP | 0.55 | open |  |
| 11-06 22:31 | +10 stop | SOL | UP | 0.59 | 0.40 | -2.24 |
| 11-06 22:31 | +20 | SOL | UP | 0.58 | open |  |
