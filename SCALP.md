# Range-Scalp Bot

*Updated Tue Nov 24 00:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70354 | 61406 | 8948 (147) | 2 | $-18835.70 | -4.3% |
| **+10¢** | 52489 | 42038 | 10451 (190) | 2 | $-17469.11 | -5.3% |
| **+15¢** | 43970 | 32714 | 11256 (246) | 3 | $-15556.12 | -5.6% |
| **+20¢** | 39148 | 27301 | 11847 (311) | 5 | $-13926.69 | -5.7% |
| **+10¢ (15¢ stop)** | 85675 | 85479 | 196 (118) | 2 | $-31510.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 00:42 | +15 | BNB | UP | 0.67 | open |  |
| 11-24 00:42 | +10 | BNB | UP | 0.67 | open |  |
| 11-24 00:42 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-24 00:42 | +20 | BNB | UP | 0.71 | open |  |
| 11-24 00:42 | +5 | BNB | UP | 0.70 | open |  |
| 11-24 00:42 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 11-24 00:41 | +10 stop | HYPE | DOWN | 0.49 | 0.63 | 1.05 |
| 11-24 00:41 | +10 stop | SOL | UP | 0.66 | 0.30 | -3.91 |
| 11-24 00:41 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 11-24 00:41 | +10 | ETH | UP | 0.71 | 0.84 | 1.05 |
| 11-24 00:41 | +5 | ETH | UP | 0.71 | 0.80 | 0.63 |
| 11-24 00:40 | +5 | HYPE | DOWN | 0.59 | 0.77 | 1.50 |
| 11-24 00:40 | +10 stop | BTC | DOWN | 0.56 | 0.37 | -2.25 |
| 11-24 00:39 | +10 stop | ETH | DOWN | 0.60 | 0.37 | -2.64 |
| 11-24 00:39 | +10 stop | ZEC | DOWN | 0.62 | 0.29 | -3.62 |
| 11-24 00:39 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-24 00:39 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-24 00:39 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-24 00:39 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-24 00:39 | +10 stop | SOL | UP | 0.66 | 0.77 | 0.81 |
| 11-24 00:39 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.87 |
| 11-24 00:39 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-24 00:39 | +15 | HYPE | DOWN | 0.57 | 0.77 | 1.67 |
| 11-24 00:39 | +10 | HYPE | DOWN | 0.57 | 0.77 | 1.64 |
| 11-24 00:39 | +5 | HYPE | DOWN | 0.57 | 0.66 | 0.51 |
| 11-24 00:39 | +10 stop | BTC | DOWN | 0.50 | 0.63 | 0.95 |
| 11-24 00:39 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-24 00:39 | +5 | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-24 00:39 | +10 stop | XRP | UP | 0.69 | 0.46 | -2.63 |
| 11-24 00:38 | +10 stop | SOL | DOWN | 0.61 | 0.34 | -3.03 |
| 11-24 00:38 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-24 00:38 | +15 | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 11-24 00:38 | +10 | SOL | DOWN | 0.61 | 0.77 | 1.30 |
| 11-24 00:38 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 11-24 00:37 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 11-24 00:37 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-24 00:37 | +10 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 11-24 00:37 | +5 | XRP | DOWN | 0.64 | 0.76 | 0.90 |
| 11-24 00:35 | +10 stop | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-24 00:35 | +5 | XRP | DOWN | 0.57 | 0.73 | 1.28 |
