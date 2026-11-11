# Range-Scalp Bot

*Updated Wed Nov 11 21:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56235 | 49046 | 7189 (94) | 3 | $-15346.20 | -4.3% |
| **+10¢** | 42021 | 33631 | 8390 (124) | 3 | $-14308.15 | -5.4% |
| **+15¢** | 35238 | 26197 | 9041 (158) | 2 | $-12980.17 | -5.9% |
| **+20¢** | 31393 | 21907 | 9486 (208) | 2 | $-11330.38 | -5.8% |
| **+10¢ (15¢ stop)** | 68536 | 68415 | 121 (73) | 0 | $-25264.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 21:28 | +10 stop | SOL | DOWN | 0.64 | 0.46 | -2.15 |
| 11-11 21:28 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-11 21:28 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-11 21:28 | +10 | SOL | DOWN | 0.65 | open |  |
| 11-11 21:28 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-11 21:27 | +10 stop | BNB | UP | 0.66 | 0.85 | 1.65 |
| 11-11 21:27 | +10 stop | ETH | DOWN | 0.57 | 0.23 | -3.71 |
| 11-11 21:27 | +10 stop | BTC | DOWN | 0.64 | 0.45 | -2.25 |
| 11-11 21:26 | +5 | BTC | DOWN | 0.57 | open |  |
| 11-11 21:26 | +5 | BNB | DOWN | 0.51 | open |  |
| 11-11 21:26 | +10 stop | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 11-11 21:26 | +10 stop | BNB | DOWN | 0.59 | 0.38 | -2.44 |
| 11-11 21:24 | +5 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-11 21:24 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 11-11 21:24 | +10 stop | ETH | UP | 0.51 | 0.29 | -2.53 |
| 11-11 21:24 | +20 | ETH | UP | 0.51 | 0.76 | 2.19 |
| 11-11 21:24 | +15 | ETH | UP | 0.51 | 0.76 | 2.19 |
| 11-11 21:24 | +10 | ETH | UP | 0.51 | 0.76 | 2.19 |
| 11-11 21:24 | +5 | ETH | UP | 0.51 | 0.76 | 2.19 |
| 11-11 21:24 | +10 stop | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-11 21:24 | +20 | SOL | DOWN | 0.61 | 0.85 | 2.14 |
| 11-11 21:24 | +15 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-11 21:24 | +10 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-11 21:24 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 11-11 21:24 | +10 stop | BNB | UP | 0.65 | 0.40 | -2.83 |
| 11-11 21:23 | +10 stop | BTC | DOWN | 0.60 | 0.43 | -2.05 |
| 11-11 21:23 | +10 | BTC | DOWN | 0.60 | open |  |
| 11-11 21:23 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 11-11 21:23 | +10 stop | BNB | DOWN | 0.57 | 0.40 | -2.05 |
| 11-11 21:23 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-11 21:23 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-11 21:23 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-11 21:23 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 11-11 21:21 | +5 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 21:19 | +10 stop | ETH | DOWN | 0.56 | 0.68 | 0.86 |
| 11-11 21:19 | +15 | ETH | DOWN | 0.56 | 0.77 | 1.79 |
| 11-11 21:19 | +10 | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 11-11 21:19 | +5 | ETH | DOWN | 0.55 | 0.63 | 0.45 |
| 11-11 21:19 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-11 21:19 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
