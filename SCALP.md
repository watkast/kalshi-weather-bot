# Range-Scalp Bot

*Updated Mon Nov 09 10:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53555 | 46700 | 6855 (86) | 2 | $-14747.75 | -4.4% |
| **+10¢** | 40009 | 32014 | 7995 (112) | 3 | $-13727.73 | -5.5% |
| **+15¢** | 33523 | 24908 | 8615 (143) | 4 | $-12522.66 | -6.0% |
| **+20¢** | 29833 | 20796 | 9037 (189) | 4 | $-11017.15 | -5.9% |
| **+10¢ (15¢ stop)** | 65264 | 65158 | 106 (63) | 2 | $-24163.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 10:53 | +5 | BTC | UP | 0.59 | open |  |
| 11-09 10:53 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 11-09 10:52 | +5 | DOGE | DOWN | 0.52 | 0.60 | 0.45 |
| 11-09 10:52 | +10 stop | BTC | UP | 0.69 | open |  |
| 11-09 10:51 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 11-09 10:50 | +5 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 10:49 | +10 stop | DOGE | DOWN | 0.67 | 0.50 | -2.04 |
| 11-09 10:49 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-09 10:49 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-09 10:49 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-09 10:49 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-09 10:49 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 11-09 10:48 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 11-09 10:48 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-09 10:48 | +20 | BNB | UP | 0.64 | 0.84 | 1.73 |
| 11-09 10:48 | +15 | BNB | UP | 0.64 | 0.81 | 1.42 |
| 11-09 10:48 | +10 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-09 10:48 | +5 | BNB | UP | 0.64 | 0.76 | 0.90 |
| 11-09 10:47 | +10 stop | ZEC | DOWN | 0.58 | 0.77 | 1.59 |
| 11-09 10:47 | +10 stop | SOL | UP | 0.65 | 0.47 | -2.14 |
| 11-09 10:47 | +20 | SOL | UP | 0.64 | open |  |
| 11-09 10:47 | +15 | SOL | UP | 0.64 | open |  |
| 11-09 10:47 | +10 | SOL | UP | 0.64 | open |  |
| 11-09 10:47 | +5 | SOL | UP | 0.64 | open |  |
| 11-09 10:47 | +10 stop | BTC | UP | 0.71 | 0.52 | -2.23 |
| 11-09 10:47 | +20 | BTC | UP | 0.71 | open |  |
| 11-09 10:47 | +15 | BTC | UP | 0.71 | open |  |
| 11-09 10:47 | +10 | BTC | UP | 0.71 | open |  |
| 11-09 10:47 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-09 10:46 | +10 stop | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 11-09 10:46 | +20 | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 11-09 10:46 | +15 | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 11-09 10:46 | +10 | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 11-09 10:46 | +5 | NEAR | DOWN | 0.51 | 0.74 | 1.98 |
| 11-09 10:46 | +10 stop | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-09 10:46 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-09 10:46 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-09 10:46 | +10 | XRP | DOWN | 0.68 | 0.81 | 1.03 |
| 11-09 10:46 | +5 | XRP | DOWN | 0.68 | 0.75 | 0.40 |
| 11-09 10:46 | +10 stop | BNB | UP | 0.58 | 0.71 | 0.97 |
