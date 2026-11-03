# Range-Scalp Bot

*Updated Tue Nov 03 20:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46312 | 40331 | 5981 (72) | 4 | $-13286.66 | -4.6% |
| **+10¢** | 34571 | 27639 | 6932 (96) | 3 | $-12153.00 | -5.6% |
| **+15¢** | 28938 | 21482 | 7456 (124) | 4 | $-11105.30 | -6.1% |
| **+20¢** | 25706 | 17891 | 7815 (164) | 4 | $-9826.70 | -6.1% |
| **+10¢ (15¢ stop)** | 56486 | 56393 | 93 (56) | 0 | $-21166.72 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 20:38 | +10 stop | NEAR | UP | 0.65 | 0.76 | 0.81 |
| 11-03 20:38 | +10 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-03 20:38 | +5 | NEAR | UP | 0.64 | 0.70 | 0.28 |
| 11-03 20:37 | +10 stop | BTC | UP | 0.67 | 0.89 | 1.97 |
| 11-03 20:37 | +10 | SOL | DOWN | 0.70 | open |  |
| 11-03 20:37 | +5 | SOL | DOWN | 0.70 | open |  |
| 11-03 20:36 | +15 | ETH | UP | 0.59 | 0.76 | 1.40 |
| 11-03 20:36 | +10 stop | SOL | DOWN | 0.66 | 0.29 | -4.01 |
| 11-03 20:36 | +5 | BNB | UP | 0.66 | 0.74 | 0.50 |
| 11-03 20:36 | +10 stop | ETH | UP | 0.60 | 0.76 | 1.30 |
| 11-03 20:36 | +10 | ETH | UP | 0.60 | 0.76 | 1.30 |
| 11-03 20:35 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-03 20:35 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 11-03 20:35 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-03 20:35 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-03 20:35 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-03 20:35 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 11-03 20:34 | +10 stop | HYPE | UP | 0.60 | 0.78 | 1.50 |
| 11-03 20:34 | +10 | HYPE | UP | 0.59 | 0.78 | 1.56 |
| 11-03 20:34 | +5 | HYPE | UP | 0.59 | 0.68 | 0.53 |
| 11-03 20:34 | +10 stop | SOL | DOWN | 0.69 | 0.54 | -1.83 |
| 11-03 20:34 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 11-03 20:33 | +5 | ETH | DOWN | 0.63 | open |  |
| 11-03 20:33 | +5 | BTC | DOWN | 0.62 | open |  |
| 11-03 20:33 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-03 20:32 | +5 | ETH | DOWN | 0.51 | 0.60 | 0.55 |
| 11-03 20:32 | +10 stop | BNB | UP | 0.60 | 0.74 | 1.09 |
| 11-03 20:32 | +20 | BNB | UP | 0.60 | 0.96 | 3.40 |
| 11-03 20:32 | +15 | BNB | UP | 0.60 | 0.96 | 3.40 |
| 11-03 20:32 | +10 | BNB | UP | 0.61 | 0.74 | 0.99 |
| 11-03 20:32 | +5 | BNB | UP | 0.62 | 0.69 | 0.38 |
| 11-03 20:32 | +10 stop | SOL | DOWN | 0.67 | 0.45 | -2.54 |
| 11-03 20:32 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-03 20:32 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-03 20:32 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-03 20:32 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 11-03 20:32 | +10 stop | DOGE | DOWN | 0.59 | 0.15 | -4.66 |
| 11-03 20:32 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-03 20:32 | +15 | DOGE | DOWN | 0.59 | open |  |
| 11-03 20:32 | +10 | DOGE | DOWN | 0.59 | open |  |
