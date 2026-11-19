# Range-Scalp Bot

*Updated Thu Nov 19 05:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64822 | 56568 | 8254 (124) | 6 | $-17479.13 | -4.3% |
| **+10¢** | 48425 | 38770 | 9655 (165) | 7 | $-16271.22 | -5.3% |
| **+15¢** | 40606 | 30194 | 10412 (210) | 9 | $-14688.02 | -5.8% |
| **+20¢** | 36159 | 25225 | 10934 (265) | 9 | $-12993.34 | -5.7% |
| **+10¢ (15¢ stop)** | 78858 | 78694 | 164 (98) | 5 | $-28946.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 05:39 | +5 | ETH | UP | 0.62 | open |  |
| 11-19 05:38 | +10 stop | XRP | DOWN | 0.59 | open |  |
| 11-19 05:38 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-19 05:38 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-19 05:38 | +10 stop | ETH | UP | 0.58 | open |  |
| 11-19 05:38 | +20 | ETH | UP | 0.59 | open |  |
| 11-19 05:38 | +15 | ETH | UP | 0.59 | open |  |
| 11-19 05:38 | +10 | ETH | UP | 0.60 | open |  |
| 11-19 05:38 | +5 | ETH | UP | 0.60 | 0.67 | 0.37 |
| 11-19 05:38 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-19 05:38 | +10 | DOGE | DOWN | 0.63 | 0.77 | 1.10 |
| 11-19 05:38 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-19 05:38 | +10 stop | BNB | UP | 0.56 | 0.39 | -2.05 |
| 11-19 05:38 | +20 | BNB | UP | 0.56 | open |  |
| 11-19 05:38 | +15 | BNB | UP | 0.56 | open |  |
| 11-19 05:38 | +10 | BNB | UP | 0.55 | open |  |
| 11-19 05:38 | +5 | BNB | UP | 0.55 | open |  |
| 11-19 05:37 | +10 stop | XRP | UP | 0.65 | 0.45 | -2.34 |
| 11-19 05:37 | +20 | XRP | UP | 0.65 | open |  |
| 11-19 05:37 | +15 | XRP | UP | 0.65 | open |  |
| 11-19 05:37 | +10 | XRP | UP | 0.65 | open |  |
| 11-19 05:37 | +5 | XRP | UP | 0.65 | open |  |
| 11-19 05:37 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 11-19 05:37 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 11-19 05:37 | +10 stop | SOL | UP | 0.55 | open |  |
| 11-19 05:37 | +20 | SOL | UP | 0.55 | open |  |
| 11-19 05:37 | +15 | SOL | UP | 0.55 | open |  |
| 11-19 05:37 | +10 | SOL | UP | 0.55 | open |  |
| 11-19 05:37 | +10 stop | BTC | UP | 0.55 | 0.39 | -1.95 |
| 11-19 05:37 | +15 | BTC | UP | 0.54 | open |  |
| 11-19 05:37 | +10 | BTC | UP | 0.54 | open |  |
| 11-19 05:37 | +5 | BTC | UP | 0.54 | 0.59 | 0.15 |
| 11-19 05:35 | +10 stop | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-19 05:35 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 11-19 05:35 | +10 stop | SOL | UP | 0.65 | 0.79 | 1.11 |
| 11-19 05:35 | +10 stop | BNB | UP | 0.70 | 0.83 | 1.05 |
| 11-19 05:35 | +10 | BNB | UP | 0.70 | 0.83 | 1.05 |
| 11-19 05:35 | +5 | BNB | UP | 0.70 | 0.78 | 0.52 |
| 11-19 05:35 | +10 stop | ZEC | DOWN | 0.57 | 0.39 | -2.15 |
| 11-19 05:35 | +10 stop | DOGE | DOWN | 0.48 | 0.29 | -2.23 |
