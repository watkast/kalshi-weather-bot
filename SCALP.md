# Range-Scalp Bot

*Updated Sun Nov 15 22:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61343 | 53526 | 7817 (114) | 7 | $-16525.83 | -4.3% |
| **+10¢** | 45809 | 36650 | 9159 (153) | 7 | $-15524.37 | -5.4% |
| **+15¢** | 38371 | 28492 | 9879 (191) | 7 | $-14176.89 | -5.9% |
| **+20¢** | 34200 | 23838 | 10362 (243) | 7 | $-12442.33 | -5.8% |
| **+10¢ (15¢ stop)** | 74655 | 74503 | 152 (90) | 2 | $-27457.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 22:53 | +10 stop | DOGE | DOWN | 0.60 | 0.34 | -2.93 |
| 11-15 22:53 | +10 stop | SOL | DOWN | 0.53 | 0.35 | -2.14 |
| 11-15 22:53 | +5 | DOGE | DOWN | 0.60 | open |  |
| 11-15 22:53 | +10 stop | HYPE | UP | 0.60 | 0.72 | 0.90 |
| 11-15 22:52 | +10 stop | SOL | UP | 0.65 | 0.45 | -2.34 |
| 11-15 22:51 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-15 22:51 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-15 22:50 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-15 22:50 | +10 stop | SOL | DOWN | 0.53 | 0.36 | -2.05 |
| 11-15 22:50 | +10 stop | HYPE | DOWN | 0.70 | 0.48 | -2.53 |
| 11-15 22:49 | +10 stop | BNB | UP | 0.57 | open |  |
| 11-15 22:49 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 11-15 22:49 | +10 stop | XRP | DOWN | 0.71 | open |  |
| 11-15 22:49 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 11-15 22:49 | +10 | DOGE | UP | 0.58 | open |  |
| 11-15 22:49 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-15 22:49 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 22:49 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 11-15 22:49 | +15 | BTC | UP | 0.62 | open |  |
| 11-15 22:49 | +10 | BTC | UP | 0.62 | open |  |
| 11-15 22:49 | +5 | BTC | UP | 0.62 | open |  |
| 11-15 22:49 | +10 stop | ZEC | UP | 0.58 | 0.30 | -3.13 |
| 11-15 22:49 | +15 | ZEC | UP | 0.58 | open |  |
| 11-15 22:49 | +10 | ZEC | UP | 0.58 | open |  |
| 11-15 22:49 | +5 | ZEC | UP | 0.58 | open |  |
| 11-15 22:48 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.83 |
| 11-15 22:48 | +15 | BNB | UP | 0.70 | open |  |
| 11-15 22:48 | +10 | BNB | UP | 0.70 | open |  |
| 11-15 22:48 | +5 | BNB | UP | 0.70 | open |  |
| 11-15 22:48 | +5 | ETH | UP | 0.63 | open |  |
| 11-15 22:48 | +5 | DOGE | UP | 0.68 | 0.73 | 0.20 |
| 11-15 22:48 | +10 stop | HYPE | UP | 0.56 | 0.41 | -1.85 |
| 11-15 22:48 | +5 | SOL | UP | 0.65 | open |  |
| 11-15 22:48 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 11-15 22:48 | +20 | ETH | UP | 0.62 | open |  |
| 11-15 22:48 | +15 | ETH | UP | 0.62 | open |  |
| 11-15 22:48 | +10 | ETH | UP | 0.62 | open |  |
| 11-15 22:48 | +5 | ETH | UP | 0.62 | 0.67 | 0.17 |
| 11-15 22:47 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-15 22:47 | +5 | BNB | UP | 0.57 | 0.69 | 0.87 |
