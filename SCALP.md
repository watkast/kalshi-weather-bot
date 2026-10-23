# Range-Scalp Bot

*Updated Fri Oct 23 08:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30011 | 26130 | 3881 (39) | 2 | $-8811.90 | -4.7% |
| **+10¢** | 22498 | 18005 | 4493 (55) | 3 | $-7917.91 | -5.6% |
| **+15¢** | 18838 | 14009 | 4829 (78) | 5 | $-7125.28 | -6.0% |
| **+20¢** | 16677 | 11619 | 5058 (101) | 5 | $-6412.90 | -6.1% |
| **+10¢ (15¢ stop)** | 36816 | 36757 | 59 (32) | 1 | $-13831.56 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 08:37 | +5 | BTC | UP | 0.53 | 0.62 | 0.55 |
| 10-23 08:35 | +10 stop | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-23 08:35 | +10 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-23 08:35 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 10-23 08:35 | +10 stop | SOL | DOWN | 0.60 | 0.42 | -2.15 |
| 10-23 08:35 | +10 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 08:35 | +5 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 08:35 | +5 | HYPE | UP | 0.62 | open |  |
| 10-23 08:35 | +10 stop | DOGE | DOWN | 0.55 | 0.34 | -2.44 |
| 10-23 08:35 | +15 | DOGE | DOWN | 0.55 | open |  |
| 10-23 08:35 | +10 | DOGE | DOWN | 0.55 | open |  |
| 10-23 08:35 | +5 | DOGE | DOWN | 0.55 | open |  |
| 10-23 08:34 | +10 stop | BTC | UP | 0.70 | 0.53 | -2.03 |
| 10-23 08:34 | +10 | BTC | UP | 0.70 | open |  |
| 10-23 08:34 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 10-23 08:33 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-23 08:33 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-23 08:33 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-23 08:33 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-23 08:33 | +10 | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 10-23 08:33 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-23 08:32 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 08:32 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-23 08:32 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-23 08:32 | +10 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 08:32 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 10-23 08:31 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-23 08:31 | +20 | NEAR | UP | 0.64 | 0.89 | 2.26 |
| 10-23 08:31 | +15 | NEAR | UP | 0.64 | 0.82 | 1.52 |
| 10-23 08:31 | +10 | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 10-23 08:31 | +5 | NEAR | UP | 0.64 | 0.70 | 0.28 |
| 10-23 08:31 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-23 08:31 | +20 | ZEC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-23 08:31 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-23 08:31 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-23 08:31 | +5 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-23 08:31 | +10 stop | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 10-23 08:31 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-23 08:31 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-23 08:31 | +10 | XRP | DOWN | 0.63 | 0.75 | 0.89 |
