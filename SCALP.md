# Range-Scalp Bot

*Updated Mon Nov 09 02:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53184 | 46377 | 6807 (85) | 5 | $-14667.42 | -4.4% |
| **+10¢** | 39709 | 31770 | 7939 (110) | 5 | $-13656.96 | -5.5% |
| **+15¢** | 33274 | 24721 | 8553 (141) | 4 | $-12457.46 | -6.0% |
| **+20¢** | 29596 | 20628 | 8968 (186) | 6 | $-10969.76 | -5.9% |
| **+10¢ (15¢ stop)** | 64783 | 64677 | 106 (63) | 3 | $-24006.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 02:40 | +10 stop | SOL | DOWN | 0.55 | open |  |
| 11-09 02:40 | +10 stop | BNB | UP | 0.60 | open |  |
| 11-09 02:39 | +10 stop | SOL | UP | 0.67 | 0.43 | -2.77 |
| 11-09 02:39 | +10 stop | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 02:39 | +15 | BTC | DOWN | 0.66 | 0.92 | 2.42 |
| 11-09 02:39 | +10 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 02:39 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-09 02:39 | +10 | HYPE | DOWN | 0.68 | open |  |
| 11-09 02:38 | +5 | HYPE | DOWN | 0.69 | open |  |
| 11-09 02:38 | +10 stop | SOL | DOWN | 0.45 | 0.55 | 0.64 |
| 11-09 02:38 | +10 stop | ETH | DOWN | 0.47 | 0.27 | -2.32 |
| 11-09 02:38 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 11-09 02:38 | +10 stop | BNB | UP | 0.66 | 0.81 | 1.23 |
| 11-09 02:38 | +10 stop | HYPE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-09 02:38 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-09 02:38 | +20 | DOGE | UP | 0.63 | open |  |
| 11-09 02:38 | +15 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 11-09 02:38 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-09 02:38 | +5 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-09 02:37 | +10 stop | SOL | UP | 0.63 | 0.43 | -2.35 |
| 11-09 02:37 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.45 |
| 11-09 02:37 | +5 | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 11-09 02:36 | +10 stop | XRP | DOWN | 0.60 | 0.79 | 1.61 |
| 11-09 02:36 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-09 02:36 | +10 stop | ZEC | DOWN | 0.62 | 0.76 | 1.10 |
| 11-09 02:35 | +10 stop | ETH | UP | 0.66 | 0.46 | -2.34 |
| 11-09 02:35 | +10 stop | NEAR | UP | 0.65 | 0.33 | -3.50 |
| 11-09 02:35 | +10 | NEAR | UP | 0.65 | open |  |
| 11-09 02:35 | +5 | NEAR | UP | 0.67 | open |  |
| 11-09 02:34 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 11-09 02:33 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 11-09 02:33 | +10 stop | HYPE | UP | 0.62 | 0.47 | -1.85 |
| 11-09 02:33 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 11-09 02:32 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-09 02:32 | +10 stop | ETH | UP | 0.64 | 0.77 | 1.00 |
| 11-09 02:32 | +10 stop | ZEC | UP | 0.63 | 0.46 | -2.07 |
| 11-09 02:32 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 11-09 02:32 | +5 | SOL | UP | 0.71 | open |  |
| 11-09 02:32 | +10 stop | XRP | DOWN | 0.54 | 0.35 | -2.24 |
| 11-09 02:32 | +20 | XRP | DOWN | 0.54 | 0.79 | 2.20 |
