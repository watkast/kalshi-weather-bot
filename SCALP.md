# Range-Scalp Bot

*Updated Mon Nov 09 23:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54001 | 47099 | 6902 (89) | 0 | $-14760.33 | -4.3% |
| **+10¢** | 40333 | 32281 | 8052 (117) | 0 | $-13730.16 | -5.4% |
| **+15¢** | 33805 | 25126 | 8679 (149) | 0 | $-12506.82 | -5.9% |
| **+20¢** | 30094 | 20991 | 9103 (195) | 0 | $-10951.97 | -5.8% |
| **+10¢ (15¢ stop)** | 65781 | 65671 | 110 (66) | 0 | $-24355.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 23:02 | +10 stop | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-09 23:02 | +20 | HYPE | DOWN | 0.71 | 0.94 | 2.14 |
| 11-09 23:02 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-09 23:02 | +10 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-09 23:02 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-09 23:01 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-09 23:01 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-09 23:01 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 23:01 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-09 23:01 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-09 23:01 | +5 | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-09 23:01 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-09 23:01 | +20 | DOGE | DOWN | 0.71 | 0.93 | 2.00 |
| 11-09 23:01 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-09 23:01 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-09 23:01 | +5 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-09 23:01 | +10 stop | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 23:01 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.86 |
| 11-09 23:01 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 11-09 23:01 | +10 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 23:01 | +5 | SOL | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 23:01 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-09 23:01 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 11-09 23:01 | +15 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-09 23:01 | +10 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-09 23:01 | +5 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-09 23:00 | +10 stop | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 23:00 | +20 | XRP | DOWN | 0.62 | 0.88 | 2.35 |
| 11-09 23:00 | +15 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 23:00 | +10 | XRP | DOWN | 0.62 | 0.78 | 1.30 |
| 11-09 23:00 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.27 |
| 11-09 22:58 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-09 22:58 | +5 | NEAR | DOWN | 0.52 | 0.59 | 0.35 |
| 11-09 22:58 | +10 stop | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-09 22:58 | +20 | BTC | UP | 0.59 | 0.88 | 2.65 |
| 11-09 22:58 | +15 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-09 22:58 | +10 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-09 22:58 | +5 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-09 22:56 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 11-09 22:56 | +20 | SOL | DOWN | 0.64 | 0.87 | 2.05 |
