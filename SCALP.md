# Range-Scalp Bot

*Updated Sat Nov 28 12:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74663 | 65162 | 9501 (171) | 7 | $-19874.61 | -4.2% |
| **+10¢** | 55620 | 44522 | 11098 (217) | 7 | $-18496.33 | -5.3% |
| **+15¢** | 46565 | 34614 | 11951 (275) | 7 | $-16550.67 | -5.7% |
| **+20¢** | 41432 | 28847 | 12585 (343) | 6 | $-14959.29 | -5.8% |
| **+10¢ (15¢ stop)** | 90864 | 90644 | 220 (136) | 0 | $-33545.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 12:24 | +10 stop | ZEC | UP | 0.55 | 0.39 | -1.95 |
| 11-28 12:24 | +20 | ZEC | UP | 0.57 | open |  |
| 11-28 12:24 | +15 | ZEC | UP | 0.57 | open |  |
| 11-28 12:24 | +10 | ZEC | UP | 0.57 | open |  |
| 11-28 12:24 | +5 | ZEC | UP | 0.59 | open |  |
| 11-28 12:24 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-28 12:24 | +10 stop | XRP | UP | 0.65 | 0.48 | -2.04 |
| 11-28 12:24 | +20 | XRP | UP | 0.65 | open |  |
| 11-28 12:24 | +15 | XRP | UP | 0.65 | open |  |
| 11-28 12:24 | +10 | XRP | UP | 0.65 | open |  |
| 11-28 12:24 | +5 | XRP | UP | 0.66 | open |  |
| 11-28 12:23 | +5 | DOGE | UP | 0.61 | open |  |
| 11-28 12:23 | +5 | SOL | UP | 0.68 | open |  |
| 11-28 12:22 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-28 12:22 | +10 stop | DOGE | UP | 0.59 | 0.37 | -2.54 |
| 11-28 12:22 | +15 | DOGE | UP | 0.60 | open |  |
| 11-28 12:22 | +10 | DOGE | UP | 0.61 | open |  |
| 11-28 12:22 | +5 | DOGE | UP | 0.59 | 0.65 | 0.29 |
| 11-28 12:21 | +5 | SOL | UP | 0.58 | 0.67 | 0.56 |
| 11-28 12:21 | +10 stop | BNB | UP | 0.67 | 0.51 | -1.94 |
| 11-28 12:21 | +10 | BNB | UP | 0.67 | open |  |
| 11-28 12:21 | +5 | BNB | UP | 0.67 | open |  |
| 11-28 12:21 | +10 stop | SOL | UP | 0.61 | 0.37 | -2.74 |
| 11-28 12:21 | +10 | SOL | UP | 0.61 | open |  |
| 11-28 12:21 | +5 | SOL | UP | 0.61 | 0.67 | 0.27 |
| 11-28 12:21 | +10 stop | ETH | UP | 0.66 | 0.35 | -3.38 |
| 11-28 12:21 | +15 | ETH | UP | 0.66 | open |  |
| 11-28 12:21 | +10 | ETH | UP | 0.66 | open |  |
| 11-28 12:21 | +5 | ETH | UP | 0.67 | open |  |
| 11-28 12:17 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 11-28 12:17 | +20 | BNB | UP | 0.71 | open |  |
| 11-28 12:17 | +15 | BNB | UP | 0.69 | open |  |
| 11-28 12:17 | +10 | BNB | UP | 0.69 | 0.81 | 0.94 |
| 11-28 12:17 | +5 | BNB | UP | 0.69 | 0.78 | 0.62 |
| 11-28 12:17 | +10 stop | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-28 12:17 | +15 | ETH | UP | 0.59 | 0.78 | 1.60 |
| 11-28 12:17 | +10 | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-28 12:17 | +5 | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-28 12:17 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 11-28 12:17 | +20 | XRP | UP | 0.70 | 0.91 | 1.85 |
