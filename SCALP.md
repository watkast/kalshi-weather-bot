# Range-Scalp Bot

*Updated Thu Nov 12 03:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56559 | 49307 | 7252 (98) | 7 | $-15562.07 | -4.4% |
| **+10¢** | 42262 | 33803 | 8459 (128) | 9 | $-14504.00 | -5.5% |
| **+15¢** | 35440 | 26330 | 9110 (162) | 9 | $-13162.20 | -5.9% |
| **+20¢** | 31574 | 22013 | 9561 (212) | 9 | $-11556.91 | -5.8% |
| **+10¢ (15¢ stop)** | 68955 | 68832 | 123 (73) | 4 | $-25474.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 03:34 | +5 | HYPE | DOWN | 0.54 | 0.67 | 0.96 |
| 11-12 03:34 | +10 stop | NEAR | DOWN | 0.48 | open |  |
| 11-12 03:34 | +10 stop | ETH | DOWN | 0.44 | 0.55 | 0.74 |
| 11-12 03:34 | +10 stop | ETH | UP | 0.45 | 0.57 | 0.84 |
| 11-12 03:33 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 03:33 | +10 stop | XRP | DOWN | 0.60 | open |  |
| 11-12 03:33 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-12 03:33 | +10 stop | BNB | DOWN | 0.61 | 0.43 | -2.15 |
| 11-12 03:33 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 11-12 03:33 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 11-12 03:33 | +20 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +15 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +10 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +5 | SOL | UP | 0.61 | open |  |
| 11-12 03:33 | +10 stop | NEAR | UP | 0.61 | 0.44 | -2.05 |
| 11-12 03:33 | +5 | NEAR | UP | 0.61 | open |  |
| 11-12 03:33 | +10 stop | DOGE | UP | 0.50 | open |  |
| 11-12 03:33 | +15 | DOGE | UP | 0.50 | open |  |
| 11-12 03:33 | +10 | DOGE | UP | 0.50 | open |  |
| 11-12 03:33 | +5 | DOGE | UP | 0.50 | 0.57 | 0.34 |
| 11-12 03:32 | +5 | HYPE | UP | 0.53 | 0.61 | 0.45 |
| 11-12 03:32 | +10 stop | XRP | UP | 0.67 | 0.50 | -2.04 |
| 11-12 03:32 | +20 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +15 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +10 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +5 | XRP | UP | 0.67 | open |  |
| 11-12 03:32 | +10 stop | ZEC | UP | 0.70 | 0.53 | -2.03 |
| 11-12 03:32 | +20 | ZEC | UP | 0.70 | open |  |
| 11-12 03:32 | +15 | ZEC | UP | 0.70 | open |  |
| 11-12 03:32 | +10 | ZEC | UP | 0.70 | open |  |
| 11-12 03:32 | +5 | ZEC | UP | 0.71 | open |  |
| 11-12 03:32 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 11-12 03:32 | +20 | BTC | UP | 0.70 | open |  |
| 11-12 03:32 | +15 | BTC | UP | 0.70 | open |  |
| 11-12 03:32 | +10 | BTC | UP | 0.70 | open |  |
| 11-12 03:32 | +5 | BTC | UP | 0.70 | open |  |
| 11-12 03:31 | +10 stop | ETH | UP | 0.71 | 0.51 | -2.33 |
| 11-12 03:31 | +20 | ETH | UP | 0.71 | open |  |
| 11-12 03:31 | +15 | ETH | UP | 0.71 | open |  |
| 11-12 03:31 | +10 | ETH | UP | 0.71 | open |  |
