# Range-Scalp Bot

*Updated Tue Nov 24 06:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70555 | 61588 | 8967 (148) | 9 | $-18831.43 | -4.2% |
| **+10¢** | 52633 | 42165 | 10468 (192) | 9 | $-17418.72 | -5.3% |
| **+15¢** | 44091 | 32816 | 11275 (248) | 9 | $-15487.03 | -5.6% |
| **+20¢** | 39264 | 27394 | 11870 (314) | 9 | $-13843.10 | -5.6% |
| **+10¢ (15¢ stop)** | 85911 | 85713 | 198 (118) | 3 | $-31587.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 06:53 | +10 stop | BNB | UP | 0.62 | open |  |
| 11-24 06:53 | +10 stop | DOGE | UP | 0.53 | open |  |
| 11-24 06:53 | +10 stop | ETH | UP | 0.68 | open |  |
| 11-24 06:53 | +5 | ETH | UP | 0.68 | open |  |
| 11-24 06:51 | +5 | DOGE | UP | 0.71 | open |  |
| 11-24 06:49 | +10 stop | ETH | UP | 0.54 | 0.70 | 1.27 |
| 11-24 06:49 | +10 stop | XRP | UP | 0.70 | 0.87 | 1.47 |
| 11-24 06:49 | +5 | ETH | UP | 0.57 | 0.70 | 0.97 |
| 11-24 06:49 | +10 stop | BNB | UP | 0.68 | 0.52 | -1.94 |
| 11-24 06:49 | +10 stop | HYPE | UP | 0.66 | 0.84 | 1.54 |
| 11-24 06:49 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-24 06:48 | +5 | ETH | DOWN | 0.54 | 0.60 | 0.25 |
| 11-24 06:48 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-24 06:48 | +5 | DOGE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-24 06:48 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 11-24 06:48 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 11-24 06:48 | +5 | XRP | DOWN | 0.63 | open |  |
| 11-24 06:47 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-24 06:47 | +5 | HYPE | DOWN | 0.59 | open |  |
| 11-24 06:47 | +10 stop | BNB | DOWN | 0.63 | 0.44 | -2.25 |
| 11-24 06:47 | +20 | BNB | DOWN | 0.61 | open |  |
| 11-24 06:47 | +15 | BNB | DOWN | 0.61 | open |  |
| 11-24 06:47 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-24 06:47 | +5 | BNB | DOWN | 0.61 | 0.69 | 0.48 |
| 11-24 06:46 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 11-24 06:46 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-24 06:46 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-24 06:46 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-24 06:46 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-24 06:46 | +10 stop | SOL | DOWN | 0.63 | 0.39 | -2.74 |
| 11-24 06:46 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-24 06:46 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-24 06:46 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-24 06:46 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-24 06:46 | +10 stop | ETH | DOWN | 0.67 | 0.44 | -2.59 |
| 11-24 06:46 | +20 | ETH | DOWN | 0.66 | open |  |
| 11-24 06:46 | +15 | ETH | DOWN | 0.66 | open |  |
| 11-24 06:46 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-24 06:46 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-24 06:46 | +10 stop | XRP | DOWN | 0.63 | 0.46 | -2.05 |
