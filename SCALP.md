# Range-Scalp Bot

*Updated Sun Oct 11 03:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11319 | 9761 | 1558 (23) | 3 | $-3831.50 | -5.4% |
| **+10¢** | 8575 | 6764 | 1811 (36) | 3 | $-3639.42 | -6.7% |
| **+15¢** | 7227 | 5311 | 1916 (52) | 3 | $-3077.11 | -6.8% |
| **+20¢** | 6436 | 4442 | 1994 (66) | 3 | $-2580.57 | -6.4% |
| **+10¢ (15¢ stop)** | 13941 | 13900 | 41 (25) | 1 | $-5594.29 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 03:39 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 10-11 03:38 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 10-11 03:36 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 10-11 03:32 | +10 stop | NEAR | UP | 0.53 | 0.67 | 1.06 |
| 10-11 03:32 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 10-11 03:32 | +10 stop | BNB | UP | 0.66 | 0.80 | 1.12 |
| 10-11 03:32 | +20 | BNB | UP | 0.66 | 0.89 | 2.07 |
| 10-11 03:32 | +15 | BNB | UP | 0.66 | 0.82 | 1.33 |
| 10-11 03:32 | +10 | BNB | UP | 0.66 | 0.80 | 1.12 |
| 10-11 03:32 | +5 | BNB | UP | 0.66 | 0.71 | 0.19 |
| 10-11 03:31 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-11 03:31 | +10 stop | XRP | DOWN | 0.69 | 0.49 | -2.33 |
| 10-11 03:31 | +20 | XRP | DOWN | 0.69 | open |  |
| 10-11 03:31 | +15 | XRP | DOWN | 0.69 | open |  |
| 10-11 03:31 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-11 03:31 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-11 03:31 | +10 stop | NEAR | DOWN | 0.60 | 0.41 | -2.24 |
| 10-11 03:31 | +20 | NEAR | DOWN | 0.60 | open |  |
| 10-11 03:31 | +15 | NEAR | DOWN | 0.60 | open |  |
| 10-11 03:31 | +10 | NEAR | DOWN | 0.60 | open |  |
| 10-11 03:31 | +5 | NEAR | DOWN | 0.60 | open |  |
| 10-11 03:31 | +10 stop | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-11 03:31 | +20 | BTC | UP | 0.61 | 0.81 | 1.72 |
| 10-11 03:31 | +15 | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-11 03:31 | +10 | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-11 03:31 | +5 | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-11 03:31 | +10 stop | HYPE | DOWN | 0.63 | 0.44 | -2.25 |
| 10-11 03:31 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-11 03:31 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-11 03:31 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-11 03:31 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.24 |
| 10-11 03:19 | +10 stop | ETH | DOWN | 0.59 | 0.83 | 2.13 |
| 10-11 03:19 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-11 03:18 | +10 stop | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-11 03:18 | +5 | ETH | UP | 0.65 | no | -6.66 |
| 10-11 03:18 | +5 | XRP | DOWN | 0.56 | 0.61 | 0.15 |
| 10-11 03:18 | +10 stop | ETH | UP | 0.63 | 0.40 | -2.64 |
| 10-11 03:18 | +15 | ETH | UP | 0.61 | no | -6.27 |
| 10-11 03:18 | +10 | ETH | UP | 0.61 | no | -6.27 |
| 10-11 03:18 | +5 | ETH | UP | 0.61 | 0.66 | 0.17 |
