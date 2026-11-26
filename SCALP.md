# Range-Scalp Bot

*Updated Thu Nov 26 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72216 | 63037 | 9179 (158) | 0 | $-19188.62 | -4.2% |
| **+10¢** | 53864 | 43144 | 10720 (203) | 2 | $-17793.55 | -5.3% |
| **+15¢** | 45097 | 33551 | 11546 (260) | 2 | $-15882.68 | -5.6% |
| **+20¢** | 40152 | 27992 | 12160 (326) | 2 | $-14275.24 | -5.7% |
| **+10¢ (15¢ stop)** | 87915 | 87706 | 209 (128) | 3 | $-32233.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 02:26 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-26 02:26 | +10 stop | DOGE | UP | 0.54 | open |  |
| 11-26 02:26 | +15 | DOGE | UP | 0.54 | open |  |
| 11-26 02:26 | +10 | DOGE | UP | 0.53 | open |  |
| 11-26 02:26 | +5 | DOGE | UP | 0.54 | 0.59 | 0.15 |
| 11-26 02:26 | +5 | NEAR | UP | 0.54 | 0.61 | 0.35 |
| 11-26 02:25 | +5 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-26 02:25 | +5 | NEAR | DOWN | 0.35 | 0.54 | 1.56 |
| 11-26 02:25 | +10 stop | HYPE | DOWN | 0.66 | open |  |
| 11-26 02:25 | +10 stop | NEAR | DOWN | 0.62 | 0.40 | -2.54 |
| 11-26 02:25 | +10 stop | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-26 02:25 | +15 | ZEC | UP | 0.56 | 0.80 | 2.10 |
| 11-26 02:25 | +10 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-26 02:25 | +5 | ZEC | UP | 0.56 | 0.66 | 0.66 |
| 11-26 02:24 | +10 stop | HYPE | UP | 0.63 | 0.48 | -1.85 |
| 11-26 02:24 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.94 |
| 11-26 02:23 | +10 stop | ZEC | UP | 0.60 | 0.79 | 1.61 |
| 11-26 02:23 | +20 | ZEC | UP | 0.61 | 0.81 | 1.72 |
| 11-26 02:23 | +15 | ZEC | UP | 0.61 | 0.79 | 1.51 |
| 11-26 02:23 | +10 | ZEC | UP | 0.61 | 0.79 | 1.51 |
| 11-26 02:23 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 11-26 02:23 | +10 stop | NEAR | UP | 0.51 | 0.61 | 0.65 |
| 11-26 02:21 | +10 stop | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 11-26 02:19 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 11-26 02:19 | +10 stop | NEAR | UP | 0.62 | 0.72 | 0.68 |
| 11-26 02:18 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.72 |
| 11-26 02:18 | +5 | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-26 02:17 | +10 stop | HYPE | DOWN | 0.51 | 0.32 | -2.28 |
| 11-26 02:17 | +20 | HYPE | DOWN | 0.51 | 0.75 | 2.04 |
| 11-26 02:17 | +15 | HYPE | DOWN | 0.52 | 0.75 | 1.98 |
| 11-26 02:17 | +10 | HYPE | DOWN | 0.53 | 0.75 | 1.88 |
| 11-26 02:17 | +5 | HYPE | DOWN | 0.53 | 0.61 | 0.45 |
| 11-26 02:17 | +10 stop | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 11-26 02:17 | +10 | ZEC | UP | 0.67 | 0.77 | 0.71 |
| 11-26 02:17 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 11-26 02:17 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 11-26 02:17 | +10 stop | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-26 02:17 | +10 | SOL | UP | 0.64 | 0.76 | 0.90 |
| 11-26 02:17 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 11-26 02:17 | +10 stop | ETH | UP | 0.61 | 0.76 | 1.20 |
