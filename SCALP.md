# Range-Scalp Bot

*Updated Tue Nov 10 21:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54902 | 47884 | 7018 (94) | 6 | $-14973.40 | -4.3% |
| **+10¢** | 41020 | 32833 | 8187 (124) | 7 | $-13892.31 | -5.4% |
| **+15¢** | 34387 | 25567 | 8820 (158) | 6 | $-12601.06 | -5.8% |
| **+20¢** | 30613 | 21358 | 9255 (207) | 7 | $-11032.06 | -5.7% |
| **+10¢ (15¢ stop)** | 66889 | 66771 | 118 (73) | 4 | $-24746.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 21:22 | +10 stop | XRP | DOWN | 0.48 | open |  |
| 11-10 21:22 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 11-10 21:22 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-10 21:22 | +10 stop | HYPE | DOWN | 0.57 | open |  |
| 11-10 21:22 | +10 stop | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-10 21:22 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-10 21:22 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 11-10 21:21 | +15 | HYPE | UP | 0.52 | open |  |
| 11-10 21:20 | +5 | NEAR | UP | 0.63 | open |  |
| 11-10 21:20 | +10 stop | BTC | UP | 0.65 | 0.48 | -2.04 |
| 11-10 21:20 | +10 | BTC | UP | 0.62 | open |  |
| 11-10 21:20 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 11-10 21:20 | +10 stop | HYPE | UP | 0.67 | 0.47 | -2.34 |
| 11-10 21:20 | +10 | HYPE | UP | 0.67 | open |  |
| 11-10 21:20 | +5 | HYPE | UP | 0.67 | open |  |
| 11-10 21:20 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-10 21:20 | +5 | BNB | UP | 0.61 | open |  |
| 11-10 21:20 | +10 stop | XRP | UP | 0.60 | 0.44 | -1.95 |
| 11-10 21:19 | +10 stop | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-10 21:19 | +10 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-10 21:19 | +15 | NEAR | UP | 0.71 | open |  |
| 11-10 21:19 | +5 | BNB | DOWN | 0.47 | 0.54 | 0.34 |
| 11-10 21:19 | +5 | DOGE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-10 21:18 | +10 stop | SOL | UP | 0.67 | 0.51 | -1.94 |
| 11-10 21:18 | +10 | SOL | UP | 0.67 | open |  |
| 11-10 21:18 | +5 | ETH | UP | 0.64 | open |  |
| 11-10 21:18 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 11-10 21:18 | +20 | HYPE | UP | 0.54 | open |  |
| 11-10 21:18 | +15 | HYPE | UP | 0.54 | 0.69 | 1.17 |
| 11-10 21:18 | +10 | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 11-10 21:18 | +5 | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 11-10 21:18 | +10 stop | NEAR | UP | 0.71 | 0.46 | -2.83 |
| 11-10 21:18 | +10 | NEAR | UP | 0.71 | open |  |
| 11-10 21:17 | +5 | SOL | UP | 0.65 | 0.70 | 0.19 |
| 11-10 21:17 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-10 21:17 | +10 stop | ETH | UP | 0.58 | 0.37 | -2.45 |
| 11-10 21:17 | +20 | ETH | UP | 0.58 | open |  |
| 11-10 21:17 | +15 | ETH | UP | 0.58 | open |  |
| 11-10 21:17 | +10 | ETH | UP | 0.59 | open |  |
| 11-10 21:17 | +5 | ETH | UP | 0.58 | 0.66 | 0.46 |
