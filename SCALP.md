# Range-Scalp Bot

*Updated Thu Nov 12 14:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57027 | 49708 | 7319 (101) | 4 | $-15715.79 | -4.4% |
| **+10¢** | 42623 | 34085 | 8538 (133) | 4 | $-14650.51 | -5.5% |
| **+15¢** | 35733 | 26545 | 9188 (167) | 6 | $-13246.08 | -5.9% |
| **+20¢** | 31836 | 22197 | 9639 (217) | 6 | $-11611.02 | -5.8% |
| **+10¢ (15¢ stop)** | 69537 | 69409 | 128 (78) | 4 | $-25684.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 14:47 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-12 14:47 | +10 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-12 14:47 | +5 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-12 14:47 | +10 stop | BTC | UP | 0.49 | 0.61 | 0.85 |
| 11-12 14:47 | +20 | BTC | UP | 0.51 | open |  |
| 11-12 14:47 | +15 | BTC | UP | 0.51 | open |  |
| 11-12 14:47 | +10 | BTC | UP | 0.51 | 0.61 | 0.65 |
| 11-12 14:47 | +5 | BTC | UP | 0.53 | 0.61 | 0.45 |
| 11-12 14:47 | +10 stop | DOGE | UP | 0.53 | open |  |
| 11-12 14:47 | +20 | DOGE | UP | 0.53 | open |  |
| 11-12 14:47 | +15 | DOGE | UP | 0.53 | open |  |
| 11-12 14:47 | +10 | DOGE | UP | 0.53 | open |  |
| 11-12 14:47 | +5 | DOGE | UP | 0.53 | open |  |
| 11-12 14:46 | +10 stop | SOL | UP | 0.62 | open |  |
| 11-12 14:46 | +20 | SOL | UP | 0.62 | open |  |
| 11-12 14:46 | +15 | SOL | UP | 0.61 | open |  |
| 11-12 14:46 | +10 | SOL | UP | 0.61 | open |  |
| 11-12 14:46 | +5 | SOL | UP | 0.61 | open |  |
| 11-12 14:46 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-12 14:46 | +20 | ETH | UP | 0.57 | open |  |
| 11-12 14:46 | +15 | ETH | UP | 0.57 | open |  |
| 11-12 14:46 | +10 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-12 14:46 | +5 | ETH | UP | 0.58 | 0.66 | 0.46 |
| 11-12 14:46 | +10 stop | ZEC | UP | 0.67 | open |  |
| 11-12 14:46 | +20 | ZEC | UP | 0.67 | open |  |
| 11-12 14:46 | +15 | ZEC | UP | 0.67 | open |  |
| 11-12 14:46 | +10 | ZEC | UP | 0.67 | open |  |
| 11-12 14:46 | +5 | ZEC | UP | 0.67 | open |  |
| 11-12 14:46 | +10 stop | XRP | UP | 0.57 | open |  |
| 11-12 14:46 | +20 | XRP | UP | 0.57 | open |  |
| 11-12 14:46 | +15 | XRP | UP | 0.57 | open |  |
| 11-12 14:46 | +10 | XRP | UP | 0.58 | open |  |
| 11-12 14:46 | +5 | XRP | UP | 0.58 | open |  |
| 11-12 14:34 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 11-12 14:34 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 11-12 14:31 | +15 | ETH | UP | 0.71 | 0.89 | 1.58 |
| 11-12 14:31 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.74 |
| 11-12 14:31 | +20 | XRP | UP | 0.69 | 0.92 | 2.04 |
| 11-12 14:31 | +15 | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-12 14:31 | +10 | XRP | UP | 0.70 | 0.80 | 0.73 |
