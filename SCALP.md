# Range-Scalp Bot

*Updated Mon Nov 16 00:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61460 | 53631 | 7829 (115) | 0 | $-16533.48 | -4.3% |
| **+10¢** | 45904 | 36730 | 9174 (156) | 0 | $-15508.72 | -5.4% |
| **+15¢** | 38457 | 28559 | 9898 (195) | 0 | $-14155.76 | -5.9% |
| **+20¢** | 34280 | 23897 | 10383 (247) | 0 | $-12414.85 | -5.8% |
| **+10¢ (15¢ stop)** | 74790 | 74636 | 154 (90) | 0 | $-27493.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 00:47 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-16 00:45 | +10 stop | HYPE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-16 00:45 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-16 00:45 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-16 00:45 | +10 | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-16 00:45 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 00:45 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-16 00:45 | +20 | BTC | UP | 0.66 | 0.87 | 1.86 |
| 11-16 00:45 | +15 | BTC | UP | 0.65 | 0.81 | 1.33 |
| 11-16 00:45 | +10 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-16 00:45 | +5 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-16 00:45 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 11-16 00:45 | +20 | BNB | UP | 0.68 | 0.91 | 2.07 |
| 11-16 00:45 | +15 | BNB | UP | 0.67 | 0.82 | 1.23 |
| 11-16 00:45 | +10 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-16 00:45 | +5 | BNB | UP | 0.67 | 0.79 | 0.92 |
| 11-16 00:38 | +10 stop | HYPE | DOWN | 0.47 | 0.59 | 0.85 |
| 11-16 00:36 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-16 00:36 | +10 stop | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 00:36 | +10 | NEAR | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 00:35 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-16 00:35 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-16 00:34 | +10 stop | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 11-16 00:34 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-16 00:34 | +10 stop | BTC | UP | 0.53 | 0.34 | -2.24 |
| 11-16 00:34 | +10 stop | BNB | UP | 0.57 | 0.39 | -2.15 |
| 11-16 00:34 | +10 stop | DOGE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-16 00:34 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-16 00:33 | +5 | XRP | DOWN | 0.60 | 0.65 | 0.17 |
| 11-16 00:33 | +10 stop | SOL | DOWN | 0.54 | 0.69 | 1.17 |
| 11-16 00:33 | +10 stop | HYPE | UP | 0.54 | 0.35 | -2.24 |
| 11-16 00:32 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-16 00:32 | +10 stop | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-16 00:32 | +20 | NEAR | DOWN | 0.55 | 0.77 | 1.89 |
| 11-16 00:32 | +15 | NEAR | DOWN | 0.55 | 0.77 | 1.89 |
| 11-16 00:32 | +10 | NEAR | DOWN | 0.55 | 0.67 | 0.86 |
| 11-16 00:32 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 11-16 00:32 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-16 00:32 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-16 00:32 | +5 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
