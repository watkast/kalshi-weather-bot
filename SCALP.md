# Range-Scalp Bot

*Updated Fri Nov 20 06:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65970 | 57575 | 8395 (124) | 2 | $-17759.91 | -4.3% |
| **+10¢** | 49263 | 39444 | 9819 (165) | 1 | $-16571.14 | -5.4% |
| **+15¢** | 41318 | 30729 | 10589 (211) | 2 | $-14925.72 | -5.8% |
| **+20¢** | 36785 | 25665 | 11120 (267) | 3 | $-13209.58 | -5.7% |
| **+10¢ (15¢ stop)** | 80342 | 80178 | 164 (98) | 0 | $-29636.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 06:26 | +10 stop | HYPE | UP | 0.44 | 0.60 | 1.25 |
| 11-20 06:26 | +5 | HYPE | UP | 0.33 | 0.60 | 2.37 |
| 11-20 06:25 | +10 stop | SOL | UP | 0.46 | 0.30 | -1.93 |
| 11-20 06:25 | +10 | SOL | UP | 0.45 | open |  |
| 11-20 06:25 | +10 stop | HYPE | UP | 0.58 | 0.70 | 0.90 |
| 11-20 06:25 | +5 | HYPE | UP | 0.58 | 0.70 | 0.90 |
| 11-20 06:24 | +10 stop | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 11-20 06:24 | +15 | DOGE | DOWN | 0.57 | 0.79 | 1.90 |
| 11-20 06:24 | +10 | DOGE | DOWN | 0.57 | 0.79 | 1.90 |
| 11-20 06:24 | +5 | DOGE | DOWN | 0.58 | 0.79 | 1.83 |
| 11-20 06:24 | +10 | BTC | UP | 0.55 | 0.66 | 0.76 |
| 11-20 06:24 | +10 stop | ETH | UP | 0.46 | 0.60 | 1.05 |
| 11-20 06:24 | +10 stop | DOGE | UP | 0.44 | 0.61 | 1.34 |
| 11-20 06:24 | +20 | DOGE | UP | 0.44 | open |  |
| 11-20 06:24 | +15 | DOGE | UP | 0.44 | 0.61 | 1.34 |
| 11-20 06:24 | +10 | DOGE | UP | 0.44 | 0.61 | 1.34 |
| 11-20 06:24 | +5 | DOGE | UP | 0.44 | 0.61 | 1.34 |
| 11-20 06:24 | +10 stop | BTC | UP | 0.66 | 0.48 | -2.14 |
| 11-20 06:24 | +5 | SOL | UP | 0.71 | open |  |
| 11-20 06:23 | +5 | BTC | UP | 0.67 | open |  |
| 11-20 06:23 | +10 stop | BTC | UP | 0.52 | 0.64 | 0.85 |
| 11-20 06:23 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 11-20 06:23 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 11-20 06:23 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 11-20 06:23 | +10 stop | SOL | UP | 0.64 | 0.46 | -2.15 |
| 11-20 06:22 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-20 06:22 | +20 | BNB | DOWN | 0.61 | 0.85 | 2.14 |
| 11-20 06:22 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 11-20 06:22 | +10 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 11-20 06:22 | +5 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 11-20 06:22 | +10 stop | ETH | DOWN | 0.58 | 0.38 | -2.35 |
| 11-20 06:22 | +20 | ETH | DOWN | 0.58 | 0.83 | 2.22 |
| 11-20 06:22 | +15 | ETH | DOWN | 0.58 | 0.83 | 2.22 |
| 11-20 06:22 | +10 | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 11-20 06:22 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 11-20 06:21 | +10 stop | HYPE | DOWN | 0.41 | 0.55 | 1.04 |
| 11-20 06:20 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 11-20 06:19 | +10 stop | HYPE | UP | 0.67 | 0.50 | -2.04 |
| 11-20 06:19 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-20 06:19 | +5 | ETH | DOWN | 0.58 | 0.70 | 0.87 |
