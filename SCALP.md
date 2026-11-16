# Range-Scalp Bot

*Updated Mon Nov 16 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61633 | 53784 | 7849 (115) | 1 | $-16554.86 | -4.3% |
| **+10¢** | 46039 | 36841 | 9198 (157) | 1 | $-15509.22 | -5.4% |
| **+15¢** | 38575 | 28653 | 9922 (196) | 1 | $-14143.40 | -5.8% |
| **+20¢** | 34386 | 23979 | 10407 (248) | 1 | $-12379.39 | -5.7% |
| **+10¢ (15¢ stop)** | 75019 | 74865 | 154 (90) | 0 | $-27629.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 03:27 | +10 stop | NEAR | DOWN | 0.52 | 0.65 | 0.96 |
| 11-16 03:26 | +10 stop | HYPE | DOWN | 0.64 | 0.91 | 2.45 |
| 11-16 03:26 | +10 stop | NEAR | UP | 0.70 | 0.37 | -3.62 |
| 11-16 03:26 | +10 | NEAR | UP | 0.70 | open |  |
| 11-16 03:26 | +5 | NEAR | UP | 0.70 | open |  |
| 11-16 03:26 | +10 stop | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 11-16 03:25 | +10 stop | ZEC | UP | 0.55 | 0.10 | -4.75 |
| 11-16 03:25 | +10 stop | HYPE | UP | 0.60 | 0.38 | -2.53 |
| 11-16 03:25 | +10 stop | XRP | UP | 0.55 | 0.40 | -1.85 |
| 11-16 03:25 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 11-16 03:23 | +10 stop | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 11-16 03:23 | +10 | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 11-16 03:23 | +5 | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 11-16 03:23 | +10 stop | ETH | UP | 0.58 | 0.34 | -2.74 |
| 11-16 03:23 | +10 stop | BTC | UP | 0.63 | 0.36 | -3.04 |
| 11-16 03:23 | +10 stop | BNB | DOWN | 0.45 | 0.29 | -1.93 |
| 11-16 03:23 | +10 stop | SOL | DOWN | 0.55 | 0.37 | -2.15 |
| 11-16 03:22 | +10 stop | HYPE | DOWN | 0.60 | 0.31 | -3.22 |
| 11-16 03:21 | +10 stop | SOL | DOWN | 0.66 | 0.49 | -2.04 |
| 11-16 03:21 | +20 | SOL | DOWN | 0.66 | 0.94 | 2.57 |
| 11-16 03:21 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 03:21 | +10 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 03:21 | +5 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 11-16 03:21 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 03:21 | +10 stop | XRP | DOWN | 0.64 | 0.48 | -1.99 |
| 11-16 03:21 | +10 stop | ZEC | DOWN | 0.66 | 0.43 | -2.64 |
| 11-16 03:20 | +10 stop | BNB | DOWN | 0.69 | 0.46 | -2.63 |
| 11-16 03:20 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 11-16 03:19 | +10 stop | ETH | DOWN | 0.67 | 0.52 | -1.84 |
| 11-16 03:19 | +10 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 11-16 03:19 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-16 03:19 | +10 stop | XRP | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 03:19 | +10 stop | ZEC | UP | 0.64 | 0.46 | -2.15 |
| 11-16 03:19 | +10 stop | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 11-16 03:19 | +10 | SOL | DOWN | 0.57 | 0.71 | 1.06 |
| 11-16 03:19 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 11-16 03:19 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-16 03:19 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-16 03:19 | +10 | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 11-16 03:19 | +5 | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
