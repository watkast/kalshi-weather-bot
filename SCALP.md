# Range-Scalp Bot

*Updated Tue Oct 20 05:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25161 | 21901 | 3260 (31) | 1 | $-7400.41 | -4.7% |
| **+10¢** | 18933 | 15167 | 3766 (46) | 1 | $-6574.73 | -5.5% |
| **+15¢** | 15849 | 11793 | 4056 (70) | 1 | $-5922.37 | -6.0% |
| **+20¢** | 14012 | 9766 | 4246 (88) | 0 | $-5326.86 | -6.1% |
| **+10¢ (15¢ stop)** | 30881 | 30829 | 52 (30) | 0 | $-11498.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 05:24 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-20 05:23 | +10 | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-20 05:23 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-20 05:23 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 05:23 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-20 05:23 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 10-20 05:23 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 05:23 | +5 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 10-20 05:23 | +10 stop | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-20 05:23 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 10-20 05:23 | +15 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-20 05:23 | +10 stop | ETH | UP | 0.63 | 0.46 | -2.05 |
| 10-20 05:23 | +10 stop | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 10-20 05:23 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 10-20 05:23 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 10-20 05:23 | +10 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 10-20 05:23 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-20 05:23 | +15 | ETH | UP | 0.66 | open |  |
| 10-20 05:23 | +10 | ETH | UP | 0.66 | open |  |
| 10-20 05:23 | +5 | ETH | UP | 0.66 | open |  |
| 10-20 05:23 | +10 stop | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-20 05:23 | +20 | HYPE | DOWN | 0.64 | 0.91 | 2.48 |
| 10-20 05:23 | +15 | HYPE | DOWN | 0.64 | 0.91 | 2.48 |
| 10-20 05:23 | +10 | HYPE | DOWN | 0.64 | 0.76 | 0.92 |
| 10-20 05:23 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-20 05:23 | +10 stop | ZEC | DOWN | 0.46 | 0.61 | 1.15 |
| 10-20 05:23 | +10 stop | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-20 05:23 | +15 | SOL | DOWN | 0.54 | 0.71 | 1.37 |
| 10-20 05:23 | +10 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-20 05:23 | +5 | SOL | DOWN | 0.54 | 0.64 | 0.65 |
| 10-20 05:21 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-20 05:20 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-20 05:20 | +10 stop | ETH | DOWN | 0.70 | 0.39 | -3.42 |
| 10-20 05:19 | +5 | ETH | DOWN | 0.62 | 0.70 | 0.48 |
| 10-20 05:19 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-20 05:19 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-20 05:17 | +10 stop | ZEC | UP | 0.53 | 0.32 | -2.44 |
| 10-20 05:17 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-20 05:17 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 10-20 05:17 | +15 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
