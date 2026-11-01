# Range-Scalp Bot

*Updated Sun Nov 01 02:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43074 | 37549 | 5525 (62) | 8 | $-12219.51 | -4.5% |
| **+10¢** | 32119 | 25732 | 6387 (84) | 6 | $-10968.66 | -5.4% |
| **+15¢** | 26869 | 19983 | 6886 (112) | 5 | $-10062.87 | -6.0% |
| **+20¢** | 23862 | 16651 | 7211 (145) | 7 | $-8880.22 | -5.9% |
| **+10¢ (15¢ stop)** | 52533 | 52450 | 83 (48) | 2 | $-19894.94 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 02:22 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-01 02:22 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-01 02:21 | +10 stop | BNB | DOWN | 0.40 | 0.54 | 1.10 |
| 11-01 02:21 | +15 | BNB | DOWN | 0.41 | 0.57 | 1.25 |
| 11-01 02:21 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 11-01 02:21 | +10 stop | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 11-01 02:21 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-01 02:21 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-01 02:21 | +10 | ZEC | UP | 0.65 | open |  |
| 11-01 02:21 | +5 | ZEC | UP | 0.65 | open |  |
| 11-01 02:21 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-01 02:21 | +10 stop | DOGE | UP | 0.63 | 0.48 | -1.85 |
| 11-01 02:21 | +20 | DOGE | UP | 0.63 | open |  |
| 11-01 02:21 | +15 | DOGE | UP | 0.62 | open |  |
| 11-01 02:21 | +10 | DOGE | UP | 0.62 | open |  |
| 11-01 02:21 | +5 | DOGE | UP | 0.62 | open |  |
| 11-01 02:20 | +10 stop | XRP | UP | 0.51 | 0.67 | 1.26 |
| 11-01 02:20 | +15 | XRP | UP | 0.51 | 0.67 | 1.26 |
| 11-01 02:20 | +10 | XRP | UP | 0.51 | 0.67 | 1.26 |
| 11-01 02:20 | +5 | XRP | UP | 0.51 | 0.67 | 1.26 |
| 11-01 02:20 | +10 stop | NEAR | UP | 0.48 | 0.30 | -2.13 |
| 11-01 02:20 | +10 stop | ETH | UP | 0.63 | 0.39 | -2.74 |
| 11-01 02:20 | +5 | ETH | UP | 0.63 | open |  |
| 11-01 02:20 | +10 stop | SOL | UP | 0.60 | 0.42 | -2.15 |
| 11-01 02:20 | +20 | SOL | UP | 0.60 | open |  |
| 11-01 02:20 | +15 | SOL | UP | 0.60 | open |  |
| 11-01 02:20 | +10 | SOL | UP | 0.60 | open |  |
| 11-01 02:20 | +5 | SOL | UP | 0.60 | open |  |
| 11-01 02:20 | +10 stop | HYPE | DOWN | 0.67 | 0.81 | 1.09 |
| 11-01 02:19 | +5 | BTC | UP | 0.71 | open |  |
| 11-01 02:19 | +5 | BNB | UP | 0.62 | open |  |
| 11-01 02:18 | +10 stop | BTC | UP | 0.71 | 0.56 | -1.83 |
| 11-01 02:18 | +5 | ETH | UP | 0.68 | 0.75 | 0.40 |
| 11-01 02:18 | +5 | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-01 02:18 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 11-01 02:17 | +10 stop | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 11-01 02:17 | +20 | ZEC | UP | 0.64 | open |  |
| 11-01 02:17 | +15 | ZEC | UP | 0.64 | open |  |
| 11-01 02:17 | +10 | ZEC | UP | 0.64 | 0.74 | 0.69 |
| 11-01 02:17 | +5 | ZEC | UP | 0.64 | 0.74 | 0.69 |
