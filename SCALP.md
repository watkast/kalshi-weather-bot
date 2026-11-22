# Range-Scalp Bot

*Updated Sun Nov 22 02:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68137 | 59465 | 8672 (138) | 0 | $-18283.65 | -4.3% |
| **+10¢** | 50872 | 40743 | 10129 (181) | 0 | $-16945.83 | -5.3% |
| **+15¢** | 42646 | 31726 | 10920 (231) | 1 | $-15198.31 | -5.7% |
| **+20¢** | 37964 | 26487 | 11477 (289) | 2 | $-13528.34 | -5.7% |
| **+10¢ (15¢ stop)** | 82950 | 82771 | 179 (111) | 0 | $-30427.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 02:33 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 11-22 02:33 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.29 |
| 11-22 02:33 | +20 | HYPE | DOWN | 0.65 | open |  |
| 11-22 02:33 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-22 02:33 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.03 |
| 11-22 02:33 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.20 |
| 11-22 02:33 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 02:33 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 02:33 | +5 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 02:32 | +10 stop | ZEC | UP | 0.57 | 0.37 | -2.34 |
| 11-22 02:32 | +10 stop | ETH | DOWN | 0.68 | 0.85 | 1.45 |
| 11-22 02:32 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-22 02:32 | +15 | ETH | DOWN | 0.68 | 0.85 | 1.45 |
| 11-22 02:32 | +10 | ETH | DOWN | 0.66 | 0.85 | 1.65 |
| 11-22 02:32 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 11-22 02:32 | +10 stop | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-22 02:32 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-22 02:32 | +15 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-22 02:32 | +10 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-22 02:32 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-22 02:32 | +10 stop | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-22 02:32 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.91 |
| 11-22 02:32 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-22 02:32 | +10 | NEAR | DOWN | 0.71 | 0.84 | 1.05 |
| 11-22 02:32 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-22 02:31 | +10 stop | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-22 02:31 | +20 | HYPE | DOWN | 0.55 | 0.77 | 1.89 |
| 11-22 02:31 | +15 | HYPE | DOWN | 0.55 | 0.77 | 1.89 |
| 11-22 02:31 | +10 | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-22 02:31 | +5 | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-22 02:31 | +5 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-22 02:31 | +20 | DOGE | DOWN | 0.70 | 0.90 | 1.78 |
| 11-22 02:31 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 02:31 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-22 02:31 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-22 02:31 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-22 02:31 | +10 stop | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 11-22 02:31 | +20 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 11-22 02:31 | +15 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
| 11-22 02:31 | +10 | XRP | DOWN | 0.57 | 0.77 | 1.69 |
