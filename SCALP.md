# Range-Scalp Bot

*Updated Sun Nov 15 18:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61082 | 53293 | 7789 (114) | 0 | $-16485.87 | -4.3% |
| **+10¢** | 45625 | 36500 | 9125 (153) | 3 | $-15490.53 | -5.4% |
| **+15¢** | 38212 | 28370 | 9842 (191) | 3 | $-14153.11 | -5.9% |
| **+20¢** | 34056 | 23733 | 10323 (243) | 4 | $-12427.02 | -5.8% |
| **+10¢ (15¢ stop)** | 74340 | 74188 | 152 (90) | 0 | $-27354.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 18:58 | +10 stop | ETH | DOWN | 0.20 | 0.52 | 2.90 |
| 11-15 18:58 | +20 | ETH | DOWN | 0.20 | 0.52 | 2.90 |
| 11-15 18:58 | +15 | ETH | DOWN | 0.20 | 0.52 | 2.90 |
| 11-15 18:58 | +10 | ETH | DOWN | 0.20 | 0.52 | 2.90 |
| 11-15 18:58 | +5 | ETH | DOWN | 0.32 | 0.52 | 1.66 |
| 11-15 18:58 | +10 stop | ZEC | DOWN | 0.58 | 0.41 | -2.05 |
| 11-15 18:58 | +5 | ZEC | DOWN | 0.58 | 0.67 | 0.56 |
| 11-15 18:58 | +10 stop | BNB | DOWN | 0.32 | 0.55 | 1.96 |
| 11-15 18:58 | +20 | BNB | DOWN | 0.32 | 0.55 | 1.96 |
| 11-15 18:58 | +15 | BNB | DOWN | 0.32 | 0.55 | 1.96 |
| 11-15 18:58 | +10 | BNB | DOWN | 0.33 | 0.55 | 1.86 |
| 11-15 18:58 | +5 | BNB | DOWN | 0.34 | 0.55 | 1.76 |
| 11-15 18:58 | +10 stop | SOL | UP | 0.48 | 0.60 | 0.85 |
| 11-15 18:58 | +10 | SOL | UP | 0.47 | 0.60 | 0.95 |
| 11-15 18:58 | +5 | SOL | UP | 0.48 | 0.60 | 0.85 |
| 11-15 18:58 | +10 stop | XRP | DOWN | 0.64 | 0.18 | -4.92 |
| 11-15 18:58 | +20 | XRP | DOWN | 0.64 | open |  |
| 11-15 18:58 | +15 | XRP | DOWN | 0.63 | open |  |
| 11-15 18:58 | +10 | XRP | DOWN | 0.63 | open |  |
| 11-15 18:58 | +5 | XRP | DOWN | 0.62 | 0.68 | 0.27 |
| 11-15 18:57 | +10 stop | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 11-15 18:57 | +15 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 11-15 18:57 | +10 | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 11-15 18:57 | +5 | NEAR | UP | 0.61 | 0.69 | 0.48 |
| 11-15 18:56 | +10 stop | SOL | UP | 0.55 | 0.68 | 0.96 |
| 11-15 18:56 | +20 | SOL | UP | 0.55 | 0.83 | 2.52 |
| 11-15 18:56 | +15 | SOL | UP | 0.55 | 0.83 | 2.52 |
| 11-15 18:56 | +10 | SOL | UP | 0.55 | 0.68 | 0.96 |
| 11-15 18:56 | +5 | SOL | UP | 0.55 | 0.68 | 0.96 |
| 11-15 18:56 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-15 18:56 | +15 | ZEC | DOWN | 0.66 | open |  |
| 11-15 18:56 | +5 | ZEC | DOWN | 0.66 | 0.78 | 0.92 |
| 11-15 18:54 | +10 stop | ZEC | DOWN | 0.71 | 0.50 | -2.43 |
| 11-15 18:54 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-15 18:54 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-15 18:53 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-15 18:53 | +10 stop | BTC | DOWN | 0.63 | 0.37 | -2.94 |
| 11-15 18:51 | +10 stop | SOL | DOWN | 0.63 | 0.85 | 1.94 |
| 11-15 18:51 | +5 | SOL | DOWN | 0.63 | 0.72 | 0.58 |
| 11-15 18:50 | +10 stop | BTC | DOWN | 0.46 | 0.62 | 1.25 |
