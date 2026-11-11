# Range-Scalp Bot

*Updated Wed Nov 11 15:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56000 | 48832 | 7168 (94) | 6 | $-15337.91 | -4.4% |
| **+10¢** | 41836 | 33475 | 8361 (124) | 8 | $-14295.35 | -5.4% |
| **+15¢** | 35079 | 26063 | 9016 (158) | 6 | $-13036.04 | -5.9% |
| **+20¢** | 31244 | 21786 | 9458 (208) | 7 | $-11410.61 | -5.8% |
| **+10¢ (15¢ stop)** | 68229 | 68108 | 121 (73) | 5 | $-25142.02 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 15:09 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-11 15:09 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-11 15:08 | +10 stop | DOGE | DOWN | 0.54 | open |  |
| 11-11 15:08 | +10 stop | ETH | UP | 0.54 | open |  |
| 11-11 15:08 | +10 stop | ZEC | DOWN | 0.65 | 0.84 | 1.62 |
| 11-11 15:08 | +5 | ZEC | DOWN | 0.65 | 0.84 | 1.62 |
| 11-11 15:07 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-11 15:07 | +10 | XRP | UP | 0.71 | open |  |
| 11-11 15:07 | +5 | XRP | UP | 0.71 | 0.79 | 0.53 |
| 11-11 15:07 | +10 stop | BTC | UP | 0.64 | 0.49 | -1.85 |
| 11-11 15:07 | +5 | BNB | DOWN | 0.55 | 0.63 | 0.45 |
| 11-11 15:06 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 11-11 15:06 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 15:06 | +15 | ZEC | DOWN | 0.65 | 0.84 | 1.64 |
| 11-11 15:06 | +5 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 15:06 | +10 stop | ETH | UP | 0.51 | 0.62 | 0.75 |
| 11-11 15:06 | +20 | HYPE | UP | 0.70 | open |  |
| 11-11 15:06 | +5 | HYPE | UP | 0.70 | open |  |
| 11-11 15:06 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 11-11 15:05 | +10 stop | NEAR | UP | 0.69 | 0.52 | -2.03 |
| 11-11 15:05 | +10 | NEAR | UP | 0.69 | open |  |
| 11-11 15:05 | +5 | NEAR | UP | 0.69 | open |  |
| 11-11 15:05 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-11 15:04 | +15 | HYPE | UP | 0.67 | open |  |
| 11-11 15:03 | +10 stop | ZEC | UP | 0.65 | 0.47 | -2.14 |
| 11-11 15:03 | +5 | ZEC | UP | 0.65 | 0.73 | 0.50 |
| 11-11 15:03 | +5 | XRP | UP | 0.58 | 0.64 | 0.25 |
| 11-11 15:03 | +10 stop | NEAR | UP | 0.59 | 0.70 | 0.73 |
| 11-11 15:03 | +20 | NEAR | UP | 0.59 | open |  |
| 11-11 15:03 | +15 | NEAR | UP | 0.59 | open |  |
| 11-11 15:03 | +10 | NEAR | UP | 0.59 | 0.70 | 0.73 |
| 11-11 15:03 | +5 | NEAR | UP | 0.59 | 0.65 | 0.22 |
| 11-11 15:03 | +10 stop | HYPE | UP | 0.70 | open |  |
| 11-11 15:03 | +10 | HYPE | UP | 0.71 | open |  |
| 11-11 15:02 | +10 | ZEC | UP | 0.70 | open |  |
| 11-11 15:02 | +5 | HYPE | UP | 0.68 | 0.77 | 0.61 |
| 11-11 15:02 | +10 stop | DOGE | UP | 0.57 | 0.39 | -2.15 |
| 11-11 15:02 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 11-11 15:02 | +20 | XRP | UP | 0.55 | 0.79 | 2.10 |
| 11-11 15:02 | +15 | XRP | UP | 0.55 | 0.70 | 1.17 |
