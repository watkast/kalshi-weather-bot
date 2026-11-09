# Range-Scalp Bot

*Updated Mon Nov 09 15:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53852 | 46973 | 6879 (86) | 5 | $-14731.96 | -4.3% |
| **+10¢** | 40222 | 32194 | 8028 (112) | 5 | $-13734.77 | -5.4% |
| **+15¢** | 33707 | 25054 | 8653 (144) | 5 | $-12512.76 | -5.9% |
| **+20¢** | 30003 | 20926 | 9077 (190) | 5 | $-10978.52 | -5.8% |
| **+10¢ (15¢ stop)** | 65614 | 65508 | 106 (63) | 0 | $-24297.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 15:28 | +10 stop | ZEC | UP | 0.59 | 0.41 | -2.14 |
| 11-09 15:28 | +20 | ZEC | UP | 0.59 | open |  |
| 11-09 15:28 | +15 | ZEC | UP | 0.59 | open |  |
| 11-09 15:28 | +10 | ZEC | UP | 0.58 | open |  |
| 11-09 15:28 | +5 | ZEC | UP | 0.54 | open |  |
| 11-09 15:25 | +10 stop | NEAR | UP | 0.65 | 0.82 | 1.43 |
| 11-09 15:25 | +10 stop | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-09 15:25 | +20 | SOL | UP | 0.66 | 0.86 | 1.75 |
| 11-09 15:25 | +15 | SOL | UP | 0.66 | 0.81 | 1.23 |
| 11-09 15:25 | +10 | SOL | UP | 0.67 | 0.81 | 1.13 |
| 11-09 15:25 | +5 | SOL | UP | 0.67 | 0.81 | 1.13 |
| 11-09 15:24 | +10 stop | BNB | UP | 0.60 | 0.81 | 1.82 |
| 11-09 15:22 | +10 stop | NEAR | UP | 0.47 | 0.59 | 0.85 |
| 11-09 15:21 | +10 stop | BNB | UP | 0.66 | 0.79 | 1.02 |
| 11-09 15:19 | +10 stop | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-09 15:19 | +10 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-09 15:19 | +5 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-09 15:18 | +10 stop | XRP | UP | 0.62 | 0.75 | 0.99 |
| 11-09 15:17 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 11-09 15:17 | +10 stop | BTC | UP | 0.62 | 0.72 | 0.68 |
| 11-09 15:17 | +10 stop | BNB | UP | 0.58 | 0.68 | 0.66 |
| 11-09 15:17 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-09 15:17 | +20 | DOGE | UP | 0.61 | 0.85 | 2.14 |
| 11-09 15:17 | +15 | DOGE | UP | 0.61 | 0.80 | 1.61 |
| 11-09 15:17 | +10 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-09 15:17 | +5 | DOGE | UP | 0.61 | 0.70 | 0.58 |
| 11-09 15:17 | +10 stop | ZEC | UP | 0.68 | 0.81 | 1.03 |
| 11-09 15:17 | +20 | ZEC | UP | 0.68 | 0.89 | 1.87 |
| 11-09 15:17 | +15 | ZEC | UP | 0.68 | 0.87 | 1.66 |
| 11-09 15:17 | +10 | ZEC | UP | 0.68 | 0.81 | 1.03 |
| 11-09 15:17 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-09 15:17 | +10 stop | SOL | UP | 0.63 | 0.87 | 2.15 |
| 11-09 15:17 | +20 | SOL | UP | 0.64 | 0.87 | 2.05 |
| 11-09 15:17 | +15 | SOL | UP | 0.64 | 0.87 | 2.05 |
| 11-09 15:17 | +10 | SOL | UP | 0.64 | 0.87 | 2.05 |
| 11-09 15:17 | +5 | SOL | UP | 0.64 | 0.71 | 0.38 |
| 11-09 15:16 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 11-09 15:16 | +20 | ETH | DOWN | 0.54 | open |  |
| 11-09 15:16 | +15 | ETH | DOWN | 0.54 | open |  |
| 11-09 15:16 | +10 | ETH | DOWN | 0.54 | open |  |
