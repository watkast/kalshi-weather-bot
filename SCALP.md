# Range-Scalp Bot

*Updated Sun Nov 08 02:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51831 | 45197 | 6634 (80) | 1 | $-14351.22 | -4.4% |
| **+10¢** | 38683 | 30948 | 7735 (106) | 7 | $-13347.61 | -5.5% |
| **+15¢** | 32391 | 24055 | 8336 (135) | 7 | $-12235.57 | -6.0% |
| **+20¢** | 28814 | 20075 | 8739 (180) | 9 | $-10770.39 | -6.0% |
| **+10¢ (15¢ stop)** | 63125 | 63022 | 103 (61) | 2 | $-23388.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 02:03 | +5 | BNB | UP | 0.59 | open |  |
| 11-08 02:03 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-08 02:03 | +5 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-08 02:03 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 11-08 02:03 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-08 02:03 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-08 02:03 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-08 02:03 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-08 02:02 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 02:02 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-08 02:02 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 11-08 02:02 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 11-08 02:02 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-08 02:02 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-08 02:02 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-08 02:02 | +10 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-08 02:02 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
| 11-08 02:02 | +5 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 02:02 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-08 02:02 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-08 02:02 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-08 02:02 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-08 02:02 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 02:01 | +10 stop | XRP | UP | 0.52 | 0.36 | -1.95 |
| 11-08 02:01 | +20 | XRP | UP | 0.52 | open |  |
| 11-08 02:01 | +15 | XRP | UP | 0.52 | open |  |
| 11-08 02:01 | +10 | XRP | UP | 0.52 | open |  |
| 11-08 02:01 | +5 | XRP | UP | 0.52 | 0.59 | 0.35 |
| 11-08 02:01 | +10 stop | SOL | UP | 0.52 | 0.34 | -2.14 |
| 11-08 02:01 | +20 | SOL | UP | 0.52 | open |  |
| 11-08 02:01 | +15 | SOL | UP | 0.51 | open |  |
| 11-08 02:01 | +10 | SOL | UP | 0.51 | open |  |
| 11-08 02:01 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 11-08 02:01 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-08 02:01 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-08 02:01 | +15 | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-08 02:01 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-08 02:01 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-08 02:01 | +10 stop | ETH | UP | 0.51 | 0.35 | -1.94 |
| 11-08 02:01 | +20 | ETH | UP | 0.51 | open |  |
