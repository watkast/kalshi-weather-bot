# Range-Scalp Bot

*Updated Mon Nov 23 12:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69972 | 61065 | 8907 (146) | 3 | $-18784.26 | -4.3% |
| **+10¢** | 52204 | 41796 | 10408 (189) | 3 | $-17481.72 | -5.3% |
| **+15¢** | 43749 | 32538 | 11211 (245) | 3 | $-15585.35 | -5.7% |
| **+20¢** | 38958 | 27160 | 11798 (310) | 3 | $-13943.26 | -5.7% |
| **+10¢ (15¢ stop)** | 85231 | 85041 | 190 (118) | 0 | $-31302.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 12:39 | +10 stop | DOGE | DOWN | 0.60 | 0.84 | 2.13 |
| 11-23 12:39 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 11-23 12:39 | +10 stop | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-23 12:38 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-23 12:38 | +10 stop | BNB | DOWN | 0.58 | 0.71 | 0.94 |
| 11-23 12:38 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-23 12:38 | +10 stop | ETH | UP | 0.60 | 0.30 | -3.32 |
| 11-23 12:38 | +5 | ETH | UP | 0.60 | open |  |
| 11-23 12:37 | +10 stop | BNB | UP | 0.60 | 0.45 | -1.85 |
| 11-23 12:37 | +10 | BNB | UP | 0.59 | open |  |
| 11-23 12:37 | +10 stop | BTC | UP | 0.53 | 0.34 | -2.24 |
| 11-23 12:37 | +10 stop | HYPE | UP | 0.51 | 0.36 | -1.85 |
| 11-23 12:37 | +20 | HYPE | UP | 0.52 | open |  |
| 11-23 12:37 | +10 | HYPE | UP | 0.52 | open |  |
| 11-23 12:37 | +5 | HYPE | UP | 0.52 | 0.57 | 0.14 |
| 11-23 12:37 | +10 stop | DOGE | UP | 0.61 | 0.35 | -2.93 |
| 11-23 12:37 | +10 stop | NEAR | UP | 0.52 | 0.35 | -2.04 |
| 11-23 12:37 | +5 | BNB | UP | 0.71 | open |  |
| 11-23 12:36 | +10 stop | DOGE | UP | 0.49 | 0.63 | 1.05 |
| 11-23 12:36 | +5 | BNB | UP | 0.55 | 0.64 | 0.55 |
| 11-23 12:36 | +10 stop | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-23 12:36 | +5 | ETH | UP | 0.53 | 0.66 | 0.96 |
| 11-23 12:35 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 11-23 12:35 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-23 12:35 | +10 stop | ZEC | UP | 0.64 | 0.47 | -2.05 |
| 11-23 12:35 | +10 stop | BNB | UP | 0.55 | 0.68 | 0.97 |
| 11-23 12:35 | +5 | BNB | UP | 0.55 | 0.64 | 0.55 |
| 11-23 12:35 | +5 | HYPE | UP | 0.66 | 0.74 | 0.50 |
| 11-23 12:34 | +10 stop | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 11-23 12:34 | +10 stop | BNB | UP | 0.55 | 0.65 | 0.66 |
| 11-23 12:34 | +10 | BNB | UP | 0.56 | 0.68 | 0.86 |
| 11-23 12:34 | +5 | BNB | UP | 0.56 | 0.65 | 0.56 |
| 11-23 12:34 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 11-23 12:34 | +5 | ETH | UP | 0.54 | 0.66 | 0.86 |
| 11-23 12:34 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-23 12:34 | +15 | HYPE | UP | 0.64 | open |  |
| 11-23 12:34 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-23 12:34 | +5 | HYPE | UP | 0.64 | 0.69 | 0.18 |
| 11-23 12:34 | +10 stop | NEAR | UP | 0.69 | 0.53 | -1.93 |
| 11-23 12:34 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
