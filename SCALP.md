# Range-Scalp Bot

*Updated Sat Nov 21 07:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67214 | 58668 | 8546 (129) | 2 | $-18012.79 | -4.3% |
| **+10¢** | 50194 | 40204 | 9990 (171) | 2 | $-16742.90 | -5.3% |
| **+15¢** | 42096 | 31326 | 10770 (219) | 2 | $-15012.00 | -5.7% |
| **+20¢** | 37469 | 26152 | 11317 (276) | 3 | $-13334.88 | -5.7% |
| **+10¢ (15¢ stop)** | 81848 | 81682 | 166 (100) | 0 | $-30125.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 07:28 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 07:28 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.37 |
| 11-21 07:27 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-21 07:27 | +10 stop | BNB | DOWN | 0.69 | 0.93 | 2.19 |
| 11-21 07:27 | +10 stop | NEAR | UP | 0.55 | 0.29 | -2.93 |
| 11-21 07:27 | +15 | NEAR | UP | 0.55 | open |  |
| 11-21 07:27 | +10 | NEAR | UP | 0.55 | open |  |
| 11-21 07:27 | +5 | NEAR | UP | 0.55 | open |  |
| 11-21 07:27 | +10 stop | DOGE | UP | 0.39 | 0.62 | 1.96 |
| 11-21 07:27 | +20 | DOGE | UP | 0.41 | 0.62 | 1.76 |
| 11-21 07:27 | +15 | DOGE | UP | 0.41 | 0.62 | 1.76 |
| 11-21 07:27 | +10 | DOGE | UP | 0.41 | 0.62 | 1.76 |
| 11-21 07:26 | +10 stop | XRP | UP | 0.68 | 0.30 | -4.11 |
| 11-21 07:26 | +10 stop | BTC | UP | 0.51 | 0.35 | -1.94 |
| 11-21 07:25 | +10 stop | BNB | UP | 0.67 | 0.52 | -1.84 |
| 11-21 07:23 | +10 stop | ETH | UP | 0.61 | 0.46 | -1.85 |
| 11-21 07:23 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 11-21 07:23 | +10 stop | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-21 07:23 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-21 07:21 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.95 |
| 11-21 07:21 | +10 stop | NEAR | DOWN | 0.64 | 0.23 | -4.40 |
| 11-21 07:21 | +10 stop | HYPE | UP | 0.71 | 0.81 | 0.74 |
| 11-21 07:21 | +10 stop | SOL | UP | 0.59 | 0.70 | 0.78 |
| 11-21 07:20 | +10 stop | ETH | UP | 0.59 | 0.70 | 0.78 |
| 11-21 07:20 | +10 stop | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 11-21 07:19 | +10 stop | XRP | DOWN | 0.65 | 0.45 | -2.34 |
| 11-21 07:19 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 11-21 07:19 | +5 | DOGE | DOWN | 0.53 | 0.71 | 1.47 |
| 11-21 07:19 | +10 stop | NEAR | DOWN | 0.53 | 0.65 | 0.86 |
| 11-21 07:19 | +10 stop | BTC | UP | 0.59 | 0.77 | 1.50 |
| 11-21 07:19 | +5 | XRP | DOWN | 0.66 | 0.75 | 0.60 |
| 11-21 07:19 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-21 07:18 | +10 stop | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 11-21 07:18 | +20 | HYPE | UP | 0.59 | 0.81 | 1.92 |
| 11-21 07:18 | +15 | HYPE | UP | 0.61 | 0.78 | 1.40 |
| 11-21 07:18 | +10 stop | BTC | UP | 0.55 | 0.66 | 0.76 |
| 11-21 07:18 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 11-21 07:18 | +10 stop | BNB | UP | 0.61 | 0.44 | -2.04 |
| 11-21 07:17 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 11-21 07:17 | +20 | ZEC | UP | 0.66 | 0.90 | 2.13 |
