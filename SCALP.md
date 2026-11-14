# Range-Scalp Bot

*Updated Sat Nov 14 07:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59144 | 51598 | 7546 (107) | 4 | $-16013.87 | -4.3% |
| **+10¢** | 44187 | 35358 | 8829 (140) | 5 | $-15039.10 | -5.4% |
| **+15¢** | 37024 | 27506 | 9518 (176) | 7 | $-13667.33 | -5.9% |
| **+20¢** | 32984 | 22991 | 9993 (228) | 6 | $-12064.18 | -5.8% |
| **+10¢ (15¢ stop)** | 71999 | 71857 | 142 (82) | 0 | $-26503.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 07:43 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 07:43 | +5 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-14 07:43 | +10 stop | HYPE | UP | 0.60 | 0.33 | -2.99 |
| 11-14 07:43 | +10 | HYPE | UP | 0.58 | open |  |
| 11-14 07:43 | +5 | HYPE | UP | 0.58 | 0.63 | 0.15 |
| 11-14 07:41 | +10 stop | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-14 07:41 | +20 | HYPE | UP | 0.59 | open |  |
| 11-14 07:41 | +15 | HYPE | UP | 0.59 | open |  |
| 11-14 07:41 | +10 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-14 07:41 | +5 | HYPE | UP | 0.59 | 0.69 | 0.68 |
| 11-14 07:38 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-14 07:38 | +10 | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-14 07:38 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 11-14 07:38 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 07:38 | +20 | XRP | DOWN | 0.69 | 0.98 | 2.72 |
| 11-14 07:38 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 07:38 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-14 07:38 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 07:38 | +10 stop | DOGE | UP | 0.53 | 0.38 | -1.85 |
| 11-14 07:38 | +15 | DOGE | UP | 0.52 | open |  |
| 11-14 07:38 | +10 | DOGE | UP | 0.52 | open |  |
| 11-14 07:38 | +5 | DOGE | UP | 0.57 | open |  |
| 11-14 07:37 | +10 stop | BNB | UP | 0.35 | 0.53 | 1.46 |
| 11-14 07:36 | +10 stop | XRP | UP | 0.64 | 0.78 | 1.10 |
| 11-14 07:36 | +15 | XRP | UP | 0.64 | open |  |
| 11-14 07:36 | +10 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 11-14 07:36 | +5 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 11-14 07:36 | +10 stop | BNB | DOWN | 0.60 | 0.44 | -1.95 |
| 11-14 07:36 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-14 07:36 | +10 | ETH | UP | 0.65 | 0.76 | 0.81 |
| 11-14 07:36 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 11-14 07:35 | +10 stop | SOL | UP | 0.59 | 0.25 | -3.71 |
| 11-14 07:35 | +10 stop | SOL | UP | 0.56 | 0.69 | 0.97 |
| 11-14 07:35 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-14 07:34 | +10 stop | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-14 07:34 | +10 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-14 07:34 | +5 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-14 07:34 | +10 stop | XRP | UP | 0.52 | 0.62 | 0.65 |
| 11-14 07:34 | +20 | XRP | UP | 0.52 | 0.78 | 2.29 |
| 11-14 07:34 | +15 | XRP | UP | 0.52 | 0.69 | 1.37 |
