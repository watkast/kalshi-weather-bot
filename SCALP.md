# Range-Scalp Bot

*Updated Sat Nov 14 02:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58891 | 51384 | 7507 (106) | 5 | $-15904.29 | -4.3% |
| **+10¢** | 43998 | 35219 | 8779 (139) | 6 | $-14882.07 | -5.4% |
| **+15¢** | 36868 | 27409 | 9459 (174) | 8 | $-13479.85 | -5.8% |
| **+20¢** | 32842 | 22911 | 9931 (226) | 9 | $-11868.08 | -5.8% |
| **+10¢ (15¢ stop)** | 71712 | 71574 | 138 (82) | 4 | $-26377.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 02:18 | +10 stop | XRP | DOWN | 0.47 | 0.58 | 0.74 |
| 11-14 02:18 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 11-14 02:18 | +10 stop | ETH | DOWN | 0.53 | open |  |
| 11-14 02:18 | +5 | NEAR | DOWN | 0.48 | 0.56 | 0.44 |
| 11-14 02:18 | +5 | XRP | DOWN | 0.47 | 0.58 | 0.74 |
| 11-14 02:17 | +10 stop | ZEC | DOWN | 0.63 | open |  |
| 11-14 02:17 | +15 | ZEC | DOWN | 0.64 | open |  |
| 11-14 02:17 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-14 02:17 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-14 02:17 | +5 | XRP | UP | 0.54 | 0.62 | 0.45 |
| 11-14 02:17 | +10 stop | DOGE | UP | 0.44 | 0.56 | 0.84 |
| 11-14 02:17 | +20 | DOGE | UP | 0.43 | open |  |
| 11-14 02:17 | +15 | DOGE | UP | 0.43 | open |  |
| 11-14 02:17 | +10 | DOGE | UP | 0.43 | 0.56 | 0.94 |
| 11-14 02:17 | +5 | DOGE | UP | 0.43 | 0.56 | 0.94 |
| 11-14 02:17 | +10 stop | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-14 02:17 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-14 02:17 | +15 | HYPE | DOWN | 0.53 | 0.68 | 1.16 |
| 11-14 02:17 | +10 | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-14 02:17 | +5 | HYPE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-14 02:17 | +5 | BNB | UP | 0.70 | open |  |
| 11-14 02:17 | +10 stop | ETH | UP | 0.66 | 0.44 | -2.54 |
| 11-14 02:17 | +10 | ETH | UP | 0.66 | open |  |
| 11-14 02:17 | +5 | ETH | UP | 0.66 | open |  |
| 11-14 02:16 | +10 stop | BNB | UP | 0.60 | 0.71 | 0.78 |
| 11-14 02:16 | +20 | BNB | UP | 0.60 | open |  |
| 11-14 02:16 | +15 | BNB | UP | 0.60 | open |  |
| 11-14 02:16 | +10 | BNB | UP | 0.60 | 0.71 | 0.78 |
| 11-14 02:16 | +5 | BNB | UP | 0.60 | 0.67 | 0.37 |
| 11-14 02:16 | +10 stop | XRP | UP | 0.58 | 0.41 | -2.05 |
| 11-14 02:16 | +20 | XRP | UP | 0.58 | open |  |
| 11-14 02:16 | +15 | XRP | UP | 0.58 | open |  |
| 11-14 02:16 | +10 | XRP | UP | 0.58 | open |  |
| 11-14 02:16 | +5 | XRP | UP | 0.58 | 0.66 | 0.46 |
| 11-14 02:16 | +10 stop | BTC | UP | 0.61 | 0.43 | -2.15 |
| 11-14 02:16 | +20 | BTC | UP | 0.61 | open |  |
| 11-14 02:16 | +15 | BTC | UP | 0.61 | open |  |
| 11-14 02:16 | +10 | BTC | UP | 0.61 | open |  |
| 11-14 02:16 | +5 | BTC | UP | 0.61 | open |  |
| 11-14 02:16 | +10 stop | ETH | UP | 0.57 | 0.67 | 0.66 |
