# Range-Scalp Bot

*Updated Sat Nov 21 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66928 | 58415 | 8513 (128) | 4 | $-17964.11 | -4.3% |
| **+10¢** | 49977 | 40027 | 9950 (170) | 5 | $-16698.08 | -5.3% |
| **+15¢** | 41907 | 31179 | 10728 (217) | 5 | $-14999.28 | -5.7% |
| **+20¢** | 37299 | 26027 | 11272 (274) | 5 | $-13323.25 | -5.7% |
| **+10¢ (15¢ stop)** | 81489 | 81323 | 166 (100) | 0 | $-30021.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 02:25 | +5 | HYPE | UP | 0.58 | 0.64 | 0.25 |
| 11-21 02:25 | +10 stop | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 11-21 02:25 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 11-21 02:25 | +10 stop | HYPE | DOWN | 0.47 | 0.32 | -1.84 |
| 11-21 02:25 | +10 | HYPE | DOWN | 0.47 | open |  |
| 11-21 02:25 | +5 | HYPE | DOWN | 0.47 | 0.52 | 0.14 |
| 11-21 02:24 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 02:24 | +15 | HYPE | DOWN | 0.55 | open |  |
| 11-21 02:24 | +10 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 02:24 | +5 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 02:23 | +5 | DOGE | DOWN | 0.61 | open |  |
| 11-21 02:23 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-21 02:23 | +10 stop | NEAR | DOWN | 0.63 | 0.43 | -2.35 |
| 11-21 02:22 | +10 stop | SOL | UP | 0.65 | 0.78 | 1.01 |
| 11-21 02:22 | +5 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-21 02:21 | +10 stop | NEAR | DOWN | 0.65 | 0.47 | -2.14 |
| 11-21 02:19 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-21 02:18 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 11-21 02:18 | +10 stop | XRP | UP | 0.56 | 0.69 | 0.97 |
| 11-21 02:18 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-21 02:18 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-21 02:18 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-21 02:17 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-21 02:17 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-21 02:17 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 11-21 02:17 | +15 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 11-21 02:17 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-21 02:17 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.50 |
| 11-21 02:17 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 11-21 02:16 | +10 stop | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-21 02:16 | +20 | HYPE | DOWN | 0.65 | open |  |
| 11-21 02:16 | +15 | HYPE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-21 02:16 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-21 02:16 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-21 02:16 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-21 02:16 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-21 02:16 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.25 |
| 11-21 02:16 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-21 02:16 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-21 02:16 | +10 stop | SOL | DOWN | 0.59 | 0.35 | -2.73 |
