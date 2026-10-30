# Range-Scalp Bot

*Updated Fri Oct 30 03:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40160 | 35083 | 5077 (51) | 4 | $-10997.80 | -4.3% |
| **+10¢** | 29923 | 24047 | 5876 (74) | 4 | $-9746.37 | -5.2% |
| **+15¢** | 25028 | 18706 | 6322 (101) | 5 | $-8721.25 | -5.5% |
| **+20¢** | 22209 | 15580 | 6629 (130) | 4 | $-7640.88 | -5.5% |
| **+10¢ (15¢ stop)** | 48983 | 48913 | 70 (37) | 1 | $-18492.54 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 03:58 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 10-30 03:56 | +10 stop | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 10-30 03:56 | +15 | HYPE | UP | 0.70 | open |  |
| 10-30 03:56 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-30 03:56 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-30 03:53 | +10 stop | BNB | UP | 0.62 | 0.81 | 1.62 |
| 10-30 03:53 | +10 stop | HYPE | UP | 0.70 | 0.38 | -3.52 |
| 10-30 03:53 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
| 10-30 03:51 | +10 stop | NEAR | DOWN | 0.65 | 0.48 | -2.04 |
| 10-30 03:51 | +5 | HYPE | UP | 0.58 | 0.64 | 0.25 |
| 10-30 03:51 | +10 stop | HYPE | UP | 0.54 | 0.64 | 0.65 |
| 10-30 03:51 | +15 | HYPE | UP | 0.54 | 0.71 | 1.37 |
| 10-30 03:51 | +5 | HYPE | UP | 0.54 | 0.61 | 0.35 |
| 10-30 03:50 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-30 03:50 | +10 stop | BTC | UP | 0.65 | 0.78 | 1.01 |
| 10-30 03:50 | +10 stop | NEAR | UP | 0.52 | 0.35 | -2.04 |
| 10-30 03:50 | +15 | ZEC | DOWN | 0.53 | 0.76 | 1.99 |
| 10-30 03:49 | +10 stop | HYPE | DOWN | 0.53 | 0.36 | -2.05 |
| 10-30 03:49 | +10 | HYPE | DOWN | 0.54 | 0.67 | 0.92 |
| 10-30 03:48 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-30 03:48 | +10 | ETH | UP | 0.67 | 0.81 | 1.13 |
| 10-30 03:48 | +5 | ETH | UP | 0.68 | 0.81 | 1.03 |
| 10-30 03:48 | +10 stop | HYPE | DOWN | 0.45 | 0.59 | 1.05 |
| 10-30 03:48 | +10 | HYPE | DOWN | 0.44 | 0.59 | 1.14 |
| 10-30 03:47 | +10 stop | BNB | UP | 0.62 | 0.80 | 1.51 |
| 10-30 03:47 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-30 03:47 | +5 | SOL | UP | 0.69 | 0.80 | 0.83 |
| 10-30 03:47 | +10 stop | HYPE | UP | 0.41 | 0.52 | 0.75 |
| 10-30 03:47 | +10 | HYPE | UP | 0.41 | 0.52 | 0.75 |
| 10-30 03:47 | +10 stop | ZEC | DOWN | 0.71 | 0.55 | -1.93 |
| 10-30 03:47 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-30 03:47 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-30 03:47 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 10-30 03:47 | +20 | ETH | UP | 0.56 | 0.81 | 2.21 |
| 10-30 03:47 | +15 | ETH | UP | 0.56 | 0.81 | 2.21 |
| 10-30 03:47 | +10 | ETH | UP | 0.57 | 0.68 | 0.76 |
| 10-30 03:47 | +5 | ETH | UP | 0.57 | 0.65 | 0.46 |
| 10-30 03:47 | +5 | XRP | UP | 0.58 | 0.64 | 0.25 |
| 10-30 03:47 | +5 | HYPE | UP | 0.60 | 0.69 | 0.58 |
| 10-30 03:46 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
